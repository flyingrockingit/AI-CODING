import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)

def hotel_chatbot():
    print(f"{Fore.CYAN}{Style.BRIGHT}🏨 WELCOME TO JEMRITI HOTEL 🏨{Style.RESET_ALL}")

    print(f"{Fore.YELLOW}We can help you with these services: 🌟")
    print("1. 🛏️ Booking a room")
    print("2. 🕐 Hotel timings")
    print("3. 🛎️ Check-in timings")
    print("4. 🧳 Check-out timings")

    choice = input(
        f"{Fore.BLACK}Please type your choice "
        f"(1=Booking, 2=Timings, 3=Check-in, 4=Check-out, or Exit): "
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

    elif choice == "exit":
        print(f"{Fore.BLUE}👋 Thank you for visiting Jemriti Hotel. Goodbye! Safe travels! ✈️")

    else:
        print(f"{Fore.YELLOW}⚠️ Sorry, I did not understand your choice.")
        print("Please enter 1, 2, 3, 4, or Exit. 😊")

hotel_chatbot()