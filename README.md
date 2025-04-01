# Repo Analyzer

**Repo Analyzer** is a Flask-based web application that simplifies understanding GitHub repositories. It connects to your GitHub account, fetches a repository’s structure and code, and provides two analysis modes powered by Google’s Gemini AI:
- **Summary Mode**: Summarizes each file’s purpose and suggests a reading flow.
- **Detailed Mode**: Analyzes each file’s code, explains its logic, and outlines its flow.

With a clean, responsive UI, it’s perfect for developers who want to quickly grasp complex repositories without exhaustive manual reading.

## Features
- GitHub OAuth authentication for secure access.
- Fetches repository structure and file contents via the GitHub API.
- AI-driven analysis with two modes: summary or detailed breakdown.
- Modern, card-based UI with scrollable results and professional styling.



## Prerequisites
- Python 3.8+
- A GitHub account
- Access to the Gemini API (or an alternative AI model API)

## Setup Instructions

1. Clone the Repository

git clone https://github.com/your-username/repo-analyzer.git
cd repo-analyzer
2. Install requirements
**pip install -r requirements.txt**

3. Configure GitHub OAuth
You’ll need to register an OAuth app on GitHub to get your CLIENT_ID and CLIENT_SECRET:

Go to GitHub Developer Settings.
Click New OAuth App.
Fill in:
Application Name: e.g., "Repo Analyzer"
Homepage URL: http://localhost:5000
Authorization Callback URL: http://localhost:5000/callback
After registering, copy the Client ID and Client Secret.
Open app.py and replace the placeholders
**CLIENT_ID = "your_github_client_id_here"
CLIENT_SECRET = "your_github_client_secret_here"**


4. Configure Gemini API Key
You’ll need a Gemini API key from Google (or replace with another AI model API):

Sign up for access at Google AI Studio (or equivalent).
Generate an API key.
Open ai_analyzer.py and replace the placeholder:
**genai.configure(api_key="your_gemini_api_key_here")**

**Not that it matters but, Repo is free to use in any form**
