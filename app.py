import streamlit as st
from api import fetch_news, analyze_sentiment, compare_sentiments, generate_tts, extract_topics_tfidf


st.title("News Sentiment Analyzer & TTS")


company_name = st.text_input("Enter Company Name")


if st.button("Analyze News"):
    if company_name:
        
        articles = fetch_news(company_name)
        st.write("Fetched Articles:", articles)

        
        sentiment_results = analyze_sentiment(articles)
        st.write("Sentiment Results:", sentiment_results)

        
        articles_with_topics = extract_topics_tfidf(sentiment_results)
        st.write("Articles with Topics:", articles_with_topics)

       
        comparison = compare_sentiments(sentiment_results)
        st.write("Comparative Sentiment Analysis:", comparison["ComparativeAnalysis"])
        st.write("Sentiment Breakdown:", comparison["SentimentCounts"])

        
        if sentiment_results:
            tts_audio = generate_tts(sentiment_results)
            st.audio(tts_audio, format="audio/mp3")
    else:
        st.warning("Please enter a company name.")
