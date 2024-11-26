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
    options = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0

    for _ in range(3):  # Best of 3 rounds
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
   
    if player_score > computer_score:
        print("Congratulations! You won the game.")
    elif computer_score > player_score:
        print("Sorry, the computer won the game.")
    else:
        print("It's a tie overall!")

if __name__ == "__main__":
    play_game()
