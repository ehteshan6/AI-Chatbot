 # app.py
import streamlit as st
from chatbot import get_bot_response
from analytics import update_analytics, show_analytics

st.set_page_config(page_title="AI Support Chatbot", layout="centered")
st.title("AI-Powered Chat Support Bot")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

user_input = st.text_input("Ask me anything about our product:", key="input")

if user_input:
    response, intent = get_bot_response(user_input)
    st.session_state.chat_history.append((user_input, response, intent))
    update_analytics(intent)

# Display chat history
for i, (user, bot, intent) in enumerate(reversed(st.session_state.chat_history)):
    st.markdown(f"**You:** {user}")
    st.markdown(f"**Bot:** {bot} _(Intent: {intent})_")
    st.markdown("---")

# Analytics 
with st.expander("View Analytics"):
    show_analytics()
