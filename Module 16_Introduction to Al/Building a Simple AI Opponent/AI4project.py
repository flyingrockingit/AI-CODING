import random 

moves = ["Rock", "Paper", "Scissors"] 
 
def display_board(): 
    print() 
    print("👾 WELCOME TO THE GAME OF ROCK, PAPER & SCISSORS 🕹️") 
    print("==============================================") 
    print("Choose your move:") 
    print("🪨  Rock") 
    print("📄 Paper") 
    print("✂️  Scissors") 
 
def ai_move(): 
    return random.choice(moves) 
 
def determine_winner(player, computer): 
    if player == computer: 
        return "draw" 
 
    elif ( 
        (player == "Rock" and computer == "Scissors") 
        or 
        (player == "Scissors" and computer == "Paper") 
        or 
        (player == "Paper" and computer == "Rock") 
    ): 
        return "player" 
 
    else: 
        return "computer" 
     
display_board() 

player_score = 0 
computer_score = 0 
 
while True: 
 
    player_move = input( 
        "\nChoose Rock, Paper, or Scissors: " 
    ).strip().capitalize() 
 
    while player_move not in moves: 
        print("❌ Invalid choice. Please stick with Rock, Paper, or Scissors.") 
 
        player_move = input( 
            "Choose Rock, Paper, or Scissors: " 
        ).strip().capitalize() 
 
    computer_move = ai_move() 
 
    print(f"\n👤 You chose: {player_move}") 
    print(f"🤖 AI robot chose: {computer_move}") 
 
    result = determine_winner(player_move, computer_move) 
 
    if result == "player": 
        print("🎉 You win!") 
        player_score += 1 
 
    elif result == "computer": 
        print("🤖 AI wins!") 
        computer_score += 1 
 
    else: 
        print("🤝 It's a draw!") 
 
    print ("\n📊 SCORE") 
    print(f"👤 You: {player_score}") 
    print(f"🤖 AI: {computer_score}") 
 
    play_again = input ( 
        "\n Do you want to play again?(yes/no):" 
    ).strip().lower() 
 
    if play_again == "no": 
        print ("\n👋 Thanks for playing this game!") 
        print ("🎮 Final score of the game:") 
        print (f"👤 You:{player_score}") 
        print (f"🤖 AI Bot: {computer_score}") 
        break