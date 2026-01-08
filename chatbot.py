import random

def simple_chatbot():
    print("ChatBot: Hi! I am a simple rule-based chatbot.")
    print("ChatBot: Ask me about the 'weather', 'time', a 'joke', or type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if "bye" in user_input or "quit" in user_input:
            print("ChatBot: Goodbye! Have a great day!")
            break # Exit the loop and end the chat

        elif "weather" in user_input:
            # Random responses for variety
            responses = ["It's sunny today!", "The weather is nice and warm.", "I think it's 20 degrees Celsius!"]
            print(f"ChatBot: {random.choice(responses)}")

        elif "time" in user_input:
            import datetime
            # Get and format the current time
            current_time = datetime.datetime.now().strftime('%H:%M')
            print(f"ChatBot: The current time is {current_time}.")

        elif "joke" in user_input:
            print("ChatBot: Why don't scientists trust atoms? Because they make up everything!")

        else:
            print("ChatBot: Sorry, I didn't understand that. Could you rephrase?")

if __name__ == "__main__":
    simple_chatbot()
