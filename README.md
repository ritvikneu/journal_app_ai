# Flask Social Media Post Generator

This application is a Flask-based web service that generates social media posts for LinkedIn, Twitter, and Reddit based on given blog content. It uses OpenAI's language model to create platform-specific posts.

## Features

- Generate social media posts for LinkedIn, Twitter, and Reddit
- Uses OpenAI's language model for content generation
- Simple web interface for input and display of results
- Docker support for easy deployment

## Prerequisites

- Python 3.9+
- Docker (for containerized deployment)
- OpenAI API key

## Installation

### Local Setup

1. Clone the repository:
   ```
   git clone https://github.com/ritvikneu/journal_app_ai

   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key as an environment variable:
   ```
   export OPENAI_API_KEY=your_api_key_here
   ```


## Usage

### Running Locally

1. Start the Flask application:
   ```
   python app.py
   ```

2. Open a web browser and navigate to `http://localhost:5001`.

3. Enter your blog content in the provided text area and submit to generate social media posts.

### Running with Docker

1. Build the Docker image:
   ```
   docker build -t flask-journal-pilot .

   ```

2. Run the Docker container:
   ```
   docker run -p 8080:5000 -e PORT=5000 -e OPENAI_API_KEY=YOUR_API_KEY flask-journal-pilot
   ```

3. Access the application at `http://localhost:8080`.

### Docker Setup on Debian VM

1. SSH into your Debian VM.

2. SCP the application to the VM

3. Install Docker by running the provided setup script setup-docker.sh:
   ```
   bash setup-docker.sh
   ```
4. Run command
    ```
   docker run -p 8080:5000 -e PORT=5000 -e OPENAI_API_KEY=YOUR_API_KEY flask-journal-pilot
   ```

## Configuration

You can modify the following in `app.py`:

- Change the OpenAI model or parameters in the `llm` initialization.
- Adjust the prompt template for different output styles.
- Modify the `SocialMediaPost` class to change the output structure.

## Deployment

The application is ready for deployment using Docker. You can push your image to a container registry and deploy it to your preferred hosting platform.

## Contributing

## License
