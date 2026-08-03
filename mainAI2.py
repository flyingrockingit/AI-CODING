from textblob import TextBlob
print ("welcome to sentimental analysis program")
user_name=input("Please enter your name:")
if not user_name:
    user_name = "Special Mystery Agent"
conversation_history = []
print (f"Hello, {user_name}! Let's analyze some text for sentiment.")
print("type 'reset', 'history' or 'exit' to reset the conversation, view history, or exit the program.")

while True:
    user_input=input(">>").strip()
    if not user_input:
        print ("please type some valid text or a valid command")
        continue
    if user_input.lower()=="exit":
        print(f"Exiting the programmme. Goodbye {user_name}")
    elif user_input.lower()== "history":
        if not conversation_history:
            print ("no conversation history yet")
        else:
            print ("conversation history")
            for idx, (text,polarity, sentiment) in enumerate(conversation_history, start =1):
                print (f"{idx}.Text{text}|Sentiement:{sentiment}")
                if sentiment == "positive":
                    print ("😊")
                elif sentiment == "negative":
                    print ("😞")
                else:
                    print("😐")
    continue
polarity=TextBlob(user_input).sentiment.polarity 
if polarity>0:
    sentiment = "positive"
elif polarity<0:
    sentiment = negative
else:
    sentiment = neutral
conversation_history.append((user_input,polarity, sentiment))
print (f"sentiment: {sentiment}Polarity:{polarity:.2f}")