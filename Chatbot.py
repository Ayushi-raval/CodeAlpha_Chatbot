"""
Basic Rule-Based Chatbot
CodeAlpha Python Programming Internship - Task 2
"""

import random
from datetime import datetime


def get_response(user_input):
    """Return the chatbot's reply for the user's message."""
    text = user_input.lower().strip()

    # Greetings
    if text in ["hello", "hi", "hey"]:
        return random.choice(["Hi!", "Hello!", "Hey there!"])

    # Asking about the bot's mood
    elif "how are you" in text:
        return "I'm fine, thanks! How about you?"

    # Asking the bot's name
    elif "your name" in text or "who are you" in text:
        return "I'm PyBot, a simple chatbot built with Python."

    # Replying to the user's mood
    elif text in ["i'm fine", "im fine", "i am fine", "good", "great", "fine"]:
        return "Glad to hear that!"

    # Current time
    elif "time" in text:
        return "The current time is " + datetime.now().strftime("%I:%M %p")

    # Current date
    elif "date" in text or "today" in text:
        return "Today's date is " + datetime.now().strftime("%d %B %Y")

    # Jokes
    elif "joke" in text:
        jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the Python programmer wear glasses? Because he couldn't C!",
            "How many programmers does it take to change a light bulb? None, it's a hardware problem!",
        ]
        return random.choice(jokes)

    # Thanks
    elif "thank" in text:
        return "You're welcome!"

    # Help menu
    elif "help" in text:
        return ("You can say hello, ask 'how are you', ask my name, "
                "ask for the time or date, or ask for a joke. Type 'bye' to exit.")

    # Anything else
    else:
        return "Sorry, I didn't understand that. Type 'help' to see what I can do."


def main():
    """Run the chat loop."""
    print("PyBot: Hi! I'm PyBot. Type 'help' to see what I can do, or 'bye' to exit.")

    while True:
        user_input = input("You: ")

        # Stop the loop when the user wants to leave
        if user_input.lower().strip() in ["bye", "goodbye", "exit", "quit"]:
            print("PyBot: Goodbye!")
            break

        print("PyBot:", get_response(user_input))


main()