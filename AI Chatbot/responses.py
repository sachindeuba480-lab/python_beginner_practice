def get_response(user_input):

    user_input = user_input.lower()

    if "hello" in user_input:
        return "Hey there!"

    elif "how are you" in user_input:
        return "I'm doing great!"

    elif "bye" in user_input:
        return "Goodbye!"

    elif "your name" in user_input:
        return "I'm a Python chatbot."

    else:
        return "I don't understand that yet."