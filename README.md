# News Sentiment Analyzer & TTS

This project analyzes news articles related to a specified company, performs sentiment analysis, and generates a Text-to-Speech (TTS) output in Hindi based on the sentiment analysis. It leverages various Natural Language Processing (NLP) techniques and third-party APIs to fetch, analyze, and summarize the news content.

## Table of Contents
1. [Project Setup](#1-project-setup)
2. [Model Details](#2-model-details)
3. [API Development](#3-api-development)
4. [API Usage](#4-api-usage)
5. [Assumptions & Limitations](#5-assumptions--limitations)

## 1. Project Setup

### Prerequisites

To run the application, you will need the following installed:

- Python 3.10 or later
- `pip` (Python package installer)

### Steps to Install and Run the Application:

1. **Clone the Repository**:
   First, clone the project repository to your local machine.

   ```bash
   git clone <repository_url>
   cd <repository_directory>
Install Dependencies: Ensure that all dependencies are installed by running the following command in your terminal.


pip install -r requirements.txt
This will install the necessary libraries, including streamlit, textblob, nltk, gTTS, deep-translator, scikit-learn, and transformers.

Run the Application: After installing the dependencies, run the application with the following command.


streamlit run app.py
This will open the Streamlit web interface in your default browser. You can now enter the company name and analyze the news related to it.

2. Model Details
2.1 Text Summarization (Topic Extraction)
This application uses TF-IDF (Term Frequency-Inverse Document Frequency) to extract the most important topics or keywords from the summaries of news articles.

Model: TfidfVectorizer from sklearn

Functionality:

Converts text summaries into vectors that represent the importance of each word in relation to the entire document set.

Extracts the top keywords from the news article summaries to highlight the main topics.

2.2 Sentiment Analysis
Sentiment analysis is performed using TextBlob, which provides a simple API to analyze the polarity of the text (positive, neutral, or negative).

Model: TextBlob Sentiment Analysis

Functionality:

Analyzes the sentiment of each news article's summary.

Assigns each article a sentiment category: Positive, Negative, or Neutral based on the polarity score.

2.3 Text-to-Speech (TTS)
The application uses the Google Text-to-Speech (gTTS) library to convert the sentiment analysis results into speech in Hindi.

Model: gTTS (Google Text-to-Speech)

Functionality:

Converts the sentiment results and topics into Hindi text.

Outputs the Hindi speech as an audio file.

3. API Development
3.1 News API
The application fetches news articles related to the given company using the NewsAPI.

API Used: NewsAPI

Endpoint: https://newsapi.org/v2/everything?q={company_name}&apiKey={my_API_KEY}

Response: A JSON response containing the fetched articles with titles and descriptions.

Integration Flow
Input: The user enters the company name via the Streamlit interface.

Fetching News: The application makes a GET request to NewsAPI to retrieve the latest articles about the company.

Analysis: Sentiment analysis and topic extraction are performed on the fetched articles.

Output: The application displays sentiment results and topics and generates TTS audio.

3.2 Third-Party APIs
NewsAPI: Used for fetching real-time news articles based on the company name.

Google TTS (gTTS): Used for generating speech based on the sentiment and topics derived from the articles.

4. API Usage
4.1 NewsAPI
Request Type: GET

URL: https://newsapi.org/v2/everything?q={company_name}&apiKey={YOUR_API_KEY}

Parameters:

q: Company name (e.g., "Apple")

apiKey: Your personal API key from NewsAPI

How to Test API via Postman:
Open Postman or any API testing tool.

Set the request type to GET and enter the URL with your company name and API key.

Send the request to receive the latest articles for the specified company.

5. Assumptions & Limitations
Assumptions
The NewsAPI will always return at least a few articles related to the company entered.

The TextBlob sentiment analysis will provide reasonable accuracy for general sentiment classification.

The user provides a valid company name, and the NewsAPI returns relevant articles.

Limitations
News Availability: If the NewsAPI fails to return relevant news articles (due to network issues or invalid API keys), no analysis will be possible.

Sentiment Analysis: The TextBlob model is simple and may not capture all nuances of sentiment, especially in articles with sarcasm or mixed sentiment.

Language Limitation in TTS: The application currently generates TTS in Hindi only. If required, additional languages can be supported by modifying the gTTS settings.

Third-Party API Limits: NewsAPI and gTTS have rate limits on their free tiers, which may restrict the number of API calls that can be made in a given time period.