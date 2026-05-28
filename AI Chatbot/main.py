from responses import get_response

print("=== AI CHATBOT ===")
print("Type 'bye' to exit.\n")

while True:

    user_message = input("You: ")

    response = get_response(user_message)

    print("Bot:", response)

    if user_message.lower() == "bye":
        break