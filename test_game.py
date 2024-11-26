from game import decide_winner

def test_tie():
    assert decide_winner("rock", "rock") == "tie"
    assert decide_winner("paper", "paper") == "tie"
    assert decide_winner("scissors", "scissors") == "tie"

def test_player_wins():
    assert decide_winner("rock", "scissors") == "player"
    assert decide_winner("scissors", "paper") == "player"
    assert decide_winner("paper", "rock") == "player"

def test_computer_wins():
    assert decide_winner("scissors", "rock") == "computer"
    assert decide_winner("paper", "scissors") == "computer"
    assert decide_winner("rock", "paper") == "computer"

def test_scoring_logic():
    player_score = 0
    computer_score = 0
    
    result = decide_winner("rock", "scissors")  # Player wins
    if result == "player":
        player_score += 1
    assert player_score == 1 and computer_score == 0

    result = decide_winner("scissors", "rock")  # Computer wins
    if result == "computer":
        computer_score += 1
    assert player_score == 1 and computer_score == 1

    result = decide_winner("rock", "rock")  # Tie
    assert player_score == 1 and computer_score == 1
