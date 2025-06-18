# Reflecta 🧠 — AI-Powered Mental Health Chatbot

Reflecta is a simple yet impactful mental health chatbot that allows users to express their emotions anonymously. It offers thoughtful, AI-generated responses based on user input, making it a safe space for those who hesitate to open up to others.This is just a base moodel of the chatbot with no memory features added an hence we can ask only a single question at a time. We have inlcuded an extra feature called sentiment analyzer that detects the sentiment of the AI responce using VADER Algorithm in the NLTK package.

This project was developed during the GenAI Hackathon held at Technopark, Trivandrum, by Team **Hexahertz** comprising of my fellow team members Anjali S Nair, Bhanupriya C P and Devika I.

## ✨ Features

- Natural conversation powered by **LLaMA3 model**
- **GroqAPI** integration for lightning-fast response generation
- Built with **Streamlit** for an intuitive web UI
- Secure API handling with `.env` file
- User-friendly interface tailored for emotional well-being

## 📦 Tech Stack

- Python
- Streamlit
- GroqAPI (LLaMA3)
- dotenv

## ⚙️ Setup Instructions

1. Clone the Repository
    ```bash
    git clone https://github.com/your-username/reflecta.git
    cd reflecta

2. Create a Virtual Environment
       python -m venv venv
       venv\Scripts\activate

3. Install Dependencies
       pip install -r requirements.txt

4. Set up your .env file
       Create a .env file in the root directory and add your Groq API key

5. Run the App
      streamlit run app.py

The chatbot will open in your browser!!!!

