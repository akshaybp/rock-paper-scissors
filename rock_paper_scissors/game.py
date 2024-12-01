import random

def decide_winner(player, computer):
    if player == computer:
        return "tie"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

def play_game():
    import random  # Ensure random is imported for this function
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    # Continue until either player or computer scores 3 points
    while player_score < 3 and computer_score < 3:
        player = input("Choose rock, paper, or scissors: ").lower()
        if player not in options:
            print("Invalid choice! Try again.")
            continue
        
        computer = random.choice(options)
        print(f"Computer chose: {computer}")
        
        result = decide_winner(player, computer)
        if result == "player":
            player_score += 1
            print("You win this round!")
        elif result == "computer":
            computer_score += 1
            print("Computer wins this round!")
        else:
            print("It's a tie!")
        
        print(f"Score: Player {player_score}, Computer {computer_score}")
    
    # Check who reached 3 points first
    if player_score == 3:
        print("Congratulations! You won the game.")
    elif computer_score == 3:
        print("Sorry, the computer won the game.")

if __name__ == "__main__":
    play_game()
