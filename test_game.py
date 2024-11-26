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
