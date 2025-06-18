import requests
from transformers import pipeline
import nltk

# Download VADER lexicon (only needs to run once)
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Your API Key directly hardcoded
GROQ_API_KEY = "enter your API key here"

# Initialize Sentiment Analyzer
sentiment_analyzer = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    scores = sentiment_analyzer.polarity_scores(text)
    sentiment = "Neutral"
    if scores["compound"] >= 0.05:
        sentiment = "Positive"
    elif scores["compound"] <= -0.05:
        sentiment = "Negative"
    return sentiment, scores["compound"]

def identify_issue(user_input):
    issues = {
        "Anxiety": ["anxious", "overwhelmed", "nervous", "panic", "worried"],
        "Burnout": ["burnout", "exhausted", "tired", "drained", "fatigue"],
        "Sleep Issues": ["not sleeping", "insomnia", "sleep", "awake", "restless"],
        "Sadness": ["sad", "cry", "depressed", "down", "unhappy"],
        "Lack of motivation": ["unmotivated", "procrastinate", "lazy"],
        "Early signs of depression":["lost interest"],
        "Work Stress": ["work", "office", "job", "boss", "deadlines", "pressure"],
        "Chronic stress": ["always on edge"],
        "Social isolation": ["disconnected","alone"],
        "Mental Fatigue": ["Can't concentrate","wandering off"],
        "Emotional eating": ["eating my feelings","not hungry"],
        "Overthinking": ["overthink"],
        "Mood swings": ["mood changes"],
        "Digital addiction": ["checking my phone frequently","overgaming"],
        "Imposter Syndrome": ["not good enough"],
        "Depressive symptoms": ["pointless","depressed","hopeless","worthlessness","loss of interest","death","suicide"],
        "Workaholism": ["guilty taking breaks"]
    }
    
    detected = []
    for issue, keywords in issues.items():
        if any(word in user_input.lower() for word in keywords):
            detected.append(issue)
    
    return detected


def query_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-70b-8192",
        "messages": [
            {"role": "system", "content": 
             "You are an empathetic mental health support bot. Users may share their feelings or situations. Analyze their problem, identify possible issues (such as anxiety, stress, insomnia, burnout, somatic symptoms, performance anxiety, chronic stress, etc.), and provide actionable, gentle suggestions like breathing exercises, journaling, sleep advice, stress management, or relaxation techniques. Be kind, supportive, professional, and avoid diagnosing or giving medical advice."
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 1024  # <-- corrected key name
    }

    response = requests.post(url, headers=headers, json=payload)

    # If error, print detailed response for debugging
    if response.status_code != 200:
        print("Error response from Groq API:", response.text)

    response.raise_for_status()

    reply = response.json()["choices"][0]["message"]["content"]
    return reply
