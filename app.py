import streamlit as st
from backend import query_groq, analyze_sentiment, identify_issue

# Inject custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #F5F5F5;
        color: #333333;
    }
    .reportview-container {
        background: #fdf6ec
    }
    .main {
        background: #ffffff;
        border-radius: 10px;
        padding: 20px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        padding: 10px 20px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("✨Reflecta | Your Thoughtful AI Guide to Mental Clarity 🌿")
st.subheader("🌿 Feel free to share your thoughts. I'm here to support you.")

# Text Input Box
user_input = st.text_area("💬 What would you like to share today?", height=150)

if st.button("🧠 Get Support"):
    if user_input.strip() == "":
        st.warning("🚨 Please enter message...")
    else:
        with st.spinner("🤔 Thinking..."):
            response = query_groq(user_input)
            sentiment, score = analyze_sentiment(response)
            issues = identify_issue(user_input)
            
        if issues:
            st.warning(f"🩺 **Possible Issues Identified:** {', '.join(issues)}")
        else:
            st.info("🩺 No specific issues detected.")


        # Show AI Response
        st.success("✅ **My Response:**")
        st.write(response)

        # Sentiment Result
        st.info(f"🧭 **Sentiment:** {sentiment} (Score: {score:.2f})")

# Footer message
st.markdown("---")
st.markdown("Made with ❤️ using **Groq + Streamlit**")
