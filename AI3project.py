import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def hotel_chatbot():
    print (f"{Style.BRIGHT + Fore.WHITE}WELCOME TO JEMRITI HOTEL 🏨{Style.RESET_ALL}")

    name = input ("What is your name?")
    print (f"Hello, {name}!😊")

    while True:
        print (f"\n{Fore.LIGHTYELLOW_EX} We can help you with these services:🌟")
        print ("1. 🛏️  Booking a room")
        print("2.  🕐  Hotel timings")
        print("3.  🛎️  Check-in timings")
        print("4.  🧳  Check-out timings")
        print ("5. 🍽️  Restaurant information")
        print ("6. 🛜  Wi-Fi Password 📶")

        choice = input (
            f"{Fore.BLACK} Please type your choice: (1,2,3,4,5,6, or Exit)"
            f"{Style.RESET_ALL}"    
        ).strip().lower()

        if choice == "1":
            print(f"{Fore.LIGHTMAGENTA_EX}🛏️ You selected Booking.")
            print("📞 Please visit the reception desk or contact our booking team.")

        elif choice == "2":
            print(f"{Fore.LIGHTCYAN_EX}🕐 Our hotel is open 24 hours a day.")

        elif choice == "3":
            print(f"{Fore.GREEN}🛎️ Check-in time is from 11:00 AM.")

        elif choice == "4":
            print(f"{Fore.RED}🧳 Check-out time is before 16:00 PM.")

        elif choice == "5":
            print (f"{Fore.LIGHTGREEN_EX}🍽️ Restaurant Timings:")
            print ("• 🥞 Breakfast timings: 7:00 - 10:00 AM 🥪")
            print ("•🍲Lunch timings: 12:30 - 14:30🍜")
            print ("•☕Tea timings: 16:00 - 16:45 PM 🫖")
            print ("•🍝 Dinnner timings: 19:00 - 22:00 PM🍲")

        elif choice == "6":
            print (f"{Fore.LIGHTRED_EX} 🛜  Wi-Fi Name: Jemriti_Home_ |📶 Password: JrSm@1805!")

        elif choice == "exit":
            print(f"{Fore.BLUE}👋 Thank you for visiting Jemriti Hotel, {name}. Goodbye! Safe travels! ✈️")
            break  

        else:
            print(f"{Fore.YELLOW}⚠️  Sorry, I did not understand your choice.")
            print("Please enter 1, 2, 3, 4, 5 or 6 or Exit. 😊")

hotel_chatbot()