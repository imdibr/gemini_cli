import os
import openai
from dotenv import load_dotenv

load_dotenv()  

openai.api_key = os.getenv("")  #initialize the api key from your personal account

conversation_history = []

def chat_with_gemini(prompt):
    try:
        response = openai.Completion.create(
            engine="text-davinci-003",  
            prompt=prompt,             
            max_tokens=150,            
            n=1,                       
            temperature=0.7,            
        )

        ai_response = response.choices[0].text.strip()  # Extract and clean the response

        # Store both user input and AI response in conversation history
        conversation_history.append({"role": "user", "content": prompt})
        conversation_history.append({"role": "gemini", "content": ai_response})

        return ai_response

    except Exception as e:
        return f"Error with the API request: {str(e)}"

def display_conversation():
    # Display the conversation history
    print("\nConversation History:")
    for entry in conversation_history:
        print(f"{entry['role'].capitalize()}: {entry['content']}")

def main():
    print("Welcome to the Google Gemini Command-Line Chatbot!")
    print("Type 'exit' to end the chat.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        response = chat_with_gemini(user_input)  
        print(f"Gemini: {response}") #display the response
        display_conversation() #shows the conversation history

if __name__ == "__main__":
    main()
