def chatbot_response(message):
    message = message.lower()

    if "hello" in message or "hi" in message:
        return "Hi there! How can I help you today?"
    elif "how are you" in message:
        return "I'm just a program, but I'm doing great! How about you?"
    elif "your name" in message:
        return "I'm ChatBot 1.0, your virtual assistant."
    elif "bye" in message or "goodbye" in message:
        return "Goodbye! Have a nice day!"
    elif "help" in message:
        return "Sure! You can ask me about basic topics like greetings, my name, or how I'm doing."
    else:
        return "I'm not sure I understand. Can you rephrase that?"

print("=== ChatBot 1.0 ===")
print("Type something to start chatting. Type 'exit' to quit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "exit":
        print("ChatBot: See you later!")
        break
    response = chatbot_response(user_input)
    print("ChatBot:", response)
