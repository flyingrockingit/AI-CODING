print("Hello there!! Welcome to Reading Hub Library. I am yours truly AAR chatbot, what is your name?")
name = input("enter name: ")

print(f"Glad to meet you today {name},\nhow may I help you out today?")

running = True
while running:
    print("\n--- Reading Hub Library Menu ---")
    print("1. Need a book?")
    print("2. Return a book?")
    print("3. Want a book summary?")
    print("4. Check my account status")
    print("5. Library hours and location")
    print("6. Exit")
    
    choice = input("Please enter your personal choice (1-6): ")
    
    if choice == "1":
        print(f"\nAwesome, {name}! What genre or the title are you looking for today?")
        genre = input("Enter genre or topic: ")
        print(f"Checking our catalog for '{genre}'... We have several great options available for checkout!")
        
    elif choice == "2":
        book_id = input("Please enter book ID: ")
        print(f"Book ID '{book_id}' returned successfully. Thank you, {name}!")
        
    elif choice == "3":
        print(f"\nI'd love to help you with that, {name}.")
        book_title = input("Which book title would you like a summary for? ")
        print(f"Generating a quick summary for '{book_title}'... (Here is a brief, spoiler-free overview!)")
        
    elif choice == "4":
        print(f"\nAccount Status for {name}:")
        print("- Active Membership: Yes")
        print("- Books currently checked out: 2")
        print("- Overdue fines: $0.00")
        
    elif choice == "5":
        print(f"\nReading Hub Library Information:")
        print("- Hours: Monday - Saturday, 9:00 AM - 8:00 PM")
        print("- Location: 123 Knowledge Way, Bookworm City")
        
    elif choice == "6":
        print(f"\nThank you for visiting Reading Hub Library, {name}. Wishing you to have a wonderful day and happy reading!")
        running = False
        break
        
    else:
        print(f"Invalid input {name}. Please choose a number between 1 and 6.")

    print("Do you wish to proceed ahead? (yes or no)")
    proceed = input()
    if proceed.lower() != "yes":
        print(f"\nThank you for visiting Reading Hub Library, {name}. Have a wonderful day!")
        running = False