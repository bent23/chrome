import random

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    print("Choose your move: Rock, Paper, or Scissors.")
    
    moves = ["rock", "paper", "scissors"]
    
    while True:
        player_choice = input("Enter your choice (rock/paper/scissors or 'quit' to stop): ").lower()
        
        if player_choice == 'quit':
            print("Thanks for playing!")
            break
        
        if player_choice not in moves:
            print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
            continue
        
        computer_choice = random.choice(moves)
        print(f"Computer chooses: {computer_choice}")
        
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "scissors" and computer_choice == "paper") or \
             (player_choice == "paper" and computer_choice == "rock"):
            print("You win!")
        else:
            print("Computer wins!")
        
        print()

rock_paper_scissors()
