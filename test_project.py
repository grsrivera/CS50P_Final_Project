import pytest, sys

from project import instructions, get_words, high_score_open, play_again, game

def test_instructions(monkeypatch):      # Test inputting anything in terminal will move on to game function
    monkeypatch.setattr("builtins.input", lambda _: "")    # Reference: https://docs.pytest.org/en/latest/how-to/monkeypatch.html
    assert instructions()==None

    monkeypatch.setattr("builtins.input", lambda _: "test")    # Reference: 1) https://docs.pytest.org/en/latest/how-to/monkeypatch.html 2) https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9
    assert instructions()==None

def test_get_words():
    assert len(get_words())>200000

def test_high_score_open():
    assert high_score_open()==10        #10 is current high score, will have to change as it changes

def test_play_again(monkeypatch):
    monkeypatch.setattr("builtins.input", lambda _: "n")    #Test that program sys.exits when user says, "no"
    with pytest.raises(SystemExit) as excinfo:
        play_again(10,5)    #Arbitrarily chose high score of 10 and score of 5

    assert str(excinfo.value)=="Thanks for playing!"

def test_game(monkeypatch, capsys):     #Testing the game function. Because it's in a while True loop, the breaks have to be uncommented in the function to be tested
    monkeypatch.setattr("builtins.input", lambda _: "!")
    game("Test word")
    captured = capsys.readouterr()                      # Reference: https://pavolkutaj.medium.com/how-to-test-printed-output-in-python-with-pytest-and-its-capsys-fixture-161010cfc5ad#:~:text=the%20function%20test_my_function%20takes%20one,fixture%20to%20capture%20the%20outputs.
    assert "Letters only!" in captured.out
