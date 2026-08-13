print("Hello! Welcome to my chatbot!")

name = input("What is your name? ")

print("Nice to meet you, " + name + "!")

mood = input("How are you feeling today? (good/bad/neutral): ")

if mood.lower() == "good":
    print("That's great to hear, " + name + "!")
elif mood.lower() == "bad":
    print("I'm sorry to hear that. I hope your day gets better!")
elif mood.lower() == "neutral":
    print("I understand. Hopefully your day gets better!")
else:
    print("Thanks for sharing how you feel!")

hobby = input("What is your favourite hobby or activity? ")

print("That's interesting! I like hearing about people's hobbies.")

reason = input("What do you like most about " + hobby + "? ")

print("That sounds like a great reason, " + name + "!")
print("It is nice that you enjoy " + hobby + " because " + reason + ".")

continue_chat = input("Would you like to continue chatting? (yes/no): ")

while continue_chat.lower() == "yes":

    question = input("What else would you like to tell me? ")

    print("Thanks for sharing that, " + name + "!")

    continue_chat = input("Would you like to continue chatting? (yes/no): ")

print("Goodbye, " + name + "!")
print("It was nice chatting with you. Have a great day!")