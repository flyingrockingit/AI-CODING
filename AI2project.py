from textblob import TextBlob

GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
RESET = "\033[0m"

print("Welcome to Sentiment Analysis Program")

user_name = input("Please enter your name: ")

if not user_name:
    user_name = "Special Mystery Agent"

conversation_history = []

print(f"Hello, {user_name}! Let's analyze some text for sentiment.")
print("Type 'reset', 'history' or 'exit' to reset the conversation, view history, or exit the program.")

while True:

    user_input = input(">> ").strip()

    if not user_input:
        print("Please type some valid text or a valid command")
        continue

    if user_input.lower() == "exit":
        print(f"Exiting the programme. Goodbye {user_name}")
        break

    elif user_input.lower() == "history":

        if not conversation_history:
            print("No conversation history yet")

        else:
            print("Conversation History")

            for idx, (text, polarity, sentiment) in enumerate(conversation_history, start=1):
                print(f"{idx}. Text: {text} | Sentiment: {sentiment}")

                if sentiment == "positive":
                    print(GREEN + "😊 Positive" + RESET)

                elif sentiment == "negative":
                    print(RED + "😞 Negative" + RESET)

                else:
                    print(YELLOW + "😐 Neutral" + RESET)

        continue

    polarity = TextBlob(user_input).sentiment.polarity

    if polarity > 0:
        sentiment = "positive"

    elif polarity < 0:
        sentiment = "negative"

    else:
        sentiment = "neutral"

    conversation_history.append((user_input, polarity, sentiment))

    if sentiment == "positive":
        print(GREEN + f"Sentiment: {sentiment} | Polarity: {polarity:.2f}" + RESET)

    elif sentiment == "negative":
        print(RED + f"Sentiment: {sentiment} | Polarity: {polarity:.2f}" + RESET)

    else:
        print(YELLOW + f"Sentiment: {sentiment} | Polarity: {polarity:.2f}" + RESET)