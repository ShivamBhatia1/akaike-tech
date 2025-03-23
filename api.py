import requests
from textblob import TextBlob
from gtts import gTTS
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk
from deep_translator import GoogleTranslator
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Download  nltk resources
nltk.download('punkt')
nltk.download('stopwords')

# stopwords in English
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
    
    tokens = word_tokenize(text.lower())
    return [word for word in tokens if word.isalnum() and word not in stop_words]

def extract_topics_tfidf(articles, num_keywords=3):
    """Extracts key topics from articles """
    summaries = [article["summary"] for article in articles if article["summary"]]
    vectorizer = TfidfVectorizer(stop_words='english', max_df=0.7)
    tfidf_matrix = vectorizer.fit_transform(summaries)
    feature_names = np.array(vectorizer.get_feature_names_out())

    
    for i, article in enumerate(articles):
        if article["summary"]:
            tfidf_vector = tfidf_matrix[i].toarray().flatten()
            top_indices = tfidf_vector.argsort()[-num_keywords:][::-1]
            article["topics"] = ", ".join(feature_names[top_indices])
    
    return articles

def fetch_news(company_name):
    """Fetches the news articles  company from NewsAPI."""
    url = f"https://newsapi.org/v2/everything?q={company_name}&apiKey=aa41e273c23f4aaab27a9d1f6fe7ca44"
    response = requests.get(url)
    
    if response.status_code == 200:
        articles = response.json().get("articles", [])[:10]
        return [{"title": art["title"], "summary": art["description"]} for art in articles]
    return []

def analyze_sentiment(articles):
    
    for article in articles:
        sentiment_score = TextBlob(article["summary"]).sentiment.polarity
        if sentiment_score > 0:
            article["sentiment"] = "Positive"
        elif sentiment_score < 0:
            article["sentiment"] = "Negative"
        else:
            article["sentiment"] = "Neutral"
    return articles

def generate_tts(sentiment_results):
    """hindi tts"""
    translator = GoogleTranslator(source='en', target='hi')
    text_summary = "न्यूज़ कवरेज का विश्लेषण। "

    for article in sentiment_results:
        title = translator.translate(article['title'])
        sentiment = translator.translate(article['sentiment'])
        text_summary += f"शीर्षक: {title}. भावना: {sentiment}. "

    tts = gTTS(text=text_summary, lang="hi", slow=False)
    audio_file = "output.mp3"
    tts.save(audio_file)
    
    return audio_file

def compare_sentiments(articles):
    """Compares ."""
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    comparisons = []

    for i in range(len(articles) - 1):
        article_1 = articles[i]
        article_2 = articles[i + 1]
        comparison = {
            "Comparison": f"Article {i+1} highlights {article_1.get('topics', 'various topics')}, "
                          f"while Article {i+2} discusses {article_2.get('topics', 'various topics')}."
        }
        comparisons.append(comparison)

    for article in articles:
        sentiment_counts[article["sentiment"]] += 1

    return {
        "SentimentCounts": sentiment_counts,
        "ComparativeAnalysis": comparisons
    }
