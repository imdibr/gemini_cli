import google.generativeai as genai
import os

# Set your Google Gemini API Key
API_KEY = "yoAIzaSyDze5nk03UDeI-OHNPXwluXGNjpj455fE8"
genai.configure(api_key=API_KEY)

def chat_with_gemini():
    print("Google Gemini CLI - Type 'exit' to quit\n")

    conversation_history = []
    
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        conversation_history.append({"role": "user", "parts": [user_input]})

        try:
            response = genai.GenerativeModel("gemini-pro").generate_content(user_input)
            bot_reply = response.text
            conversation_history.append({"role": "assistant", "parts": [bot_reply]})

            print(f"Gemini: {bot_reply}\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    chat_with_gemini()
