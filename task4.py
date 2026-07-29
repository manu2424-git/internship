def chatbot():
    print("=" * 50)
    print("        SIMPLE RULE-BASED CHATBOT")
    print("=" * 50)
    print("Type 'bye' to end the chat.\n")

    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print("Bot: Hi! Nice to meet you.")

        elif user == "how are you":
            print("Bot: I'm fine, thanks! How are you?")

        elif user == "what is your name":
            print("Bot: My name is Python Chatbot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "what can you do":
            print("Bot: I can answer simple questions and chat with you.")

        elif user == "thank you" or user == "thanks":
            print("Bot: You're welcome!")

        elif user == "bye":
            print("Bot: Goodbye! Have a great day.")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Start the chatbot
chatbot()