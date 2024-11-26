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
    player = input("Choose rock, paper, or scissors: ").lower()
    if player not in options:
        print("Invalid choice!")
        return
    computer = random.choice(options)
    print(f"Computer chose: {computer}")
    result = decide_winner(player, computer)
    print(f"Result: {result}")

if __name__ == "__main__":
    play_game()
