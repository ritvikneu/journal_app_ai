from flask import Flask, render_template, request
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.chains.llm import LLMChain
from pydantic import BaseModel, Field
import os
import re
# from urllib.parse import quote as url_quote
from langchain.llms import Ollama

# url = "https://example.com/?query=" + url_quote("some value")
app = Flask(__name__)
llm = OpenAI(temperature=0.7)
# ollama = Ollama(base_url="http://localhost:11434", model="llama3")

from langchain_groq import ChatGroq
groq_api_key = os.getenv("GROQ_API_KEY")
# llm = ChatGroq(
#     groq_api_key = groq_api_key,
#     model_name = "llama2-70b-4096"
# )


# Define the output schema
class SocialMediaPost(BaseModel):
    linkedin: str = Field(description="LinkedIn post content")
    twitter: str = Field(description="Twitter post content")
    reddit: str = Field(description="Reddit post content")

prompt_template = """
Given the following blog post content, generate three different social media posts 
suitable for LinkedIn, Twitter (X), and Reddit. Adapt the content and style for each platform.

Blog post content: {blog_content}

{format_instructions}

LinkedIn post:
Twitter post:
Reddit post:
"""
# Create the output parser
parser = PydanticOutputParser(pydantic_object=SocialMediaPost)
prompt = PromptTemplate(
    template=prompt_template,
    input_variables=["blog_content"],
    partial_variables={"format_instructions": parser.get_format_instructions()}
)

# Set up the Langchain chain
chain = LLMChain(llm=llm, prompt=prompt)
# chain = LLMChain(llm=ollama, prompt=prompt)

def extract_posts(text):
    linkedin_match = re.search(r"LinkedIn post:(.*?)(?=Twitter post:|$)", text, re.DOTALL)
    twitter_match = re.search(r"Twitter post:(.*?)(?=Reddit post:|$)", text, re.DOTALL)
    reddit_match = re.search(r"Reddit post:(.*?)$", text, re.DOTALL)

    linkedin = linkedin_match.group(1).strip() if linkedin_match else ""
    twitter = twitter_match.group(1).strip() if twitter_match else ""
    reddit = reddit_match.group(1).strip() if reddit_match else ""

    return SocialMediaPost(linkedin=linkedin, twitter=twitter, reddit=reddit)

def generate_social_media_posts(blog_content: str) -> SocialMediaPost:
    result = chain.invoke({"blog_content": blog_content})
    return extract_posts(result['text'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        blog_content = request.form['blog_content']
        try:
            posts = generate_social_media_posts(blog_content)
            return render_template('index.html', posts=posts)
        except Exception as e:
            error_message = f"An error occurred: {str(e)}"
            return render_template('index.html', error=error_message)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=False)