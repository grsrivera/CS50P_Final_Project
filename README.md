# CS50 Final Project: Hangman Game
by G Rivera

## Intro
This project is the culmination of Harvard's 10 week Introduction to Programming with Python course. For the final assignment, students are given the freedom to choose any program they will create on their own, showcasing their skills learned through the curriculum. I decided to build the classic guessing game from scratch. In addition to the standard game mechanics, I also programmed a way to create a word bank from a database, give the user hints, and save high scores. In the following, you find a video demo, installation requirements, and description of the program. Thanks for taking a look at my work!

## Video Demo
[Link](https://youtu.be/rQ5qItHykHY)

## Installation Requirements
There is only one installation requirement, which is for the word bank function.

    pip install english-words

## Description
I'll explain the rules first then explain the code for the game. The player has to guess a word randomly chosen from a word bank. They are initially presented with a set of blank spaces, shown as an underscore for each letter. They are prompted to guess a letter, and if they are correct, the underscore will be replaced with that letter; if they guess wrong the underscore remains and they lose a life.

Players start the game with 7 lives. There is no way to gain more lives. If the player needs help, they can type "hint", in which case one of the unsolved letters will be given. The player gets 3 hints for the entire game. There is no way to gain more hints. When a word is solved, the player receives points equal to the amount of letters in the word (e.g., 4 points are given for correctly guessing the word "Test"). Points are carried over to the next word if the player continues to play. The game is over when the player runs out of lives.

Next, I'll explain the functions for the word bank, game mechanics, hint system, play again screen, and scoring system,.

**Word Bank Function:** When initialized, the program creates a word bank with the english-words package. The module pulls from multiple word lists to create a set of 234,450 words. A word is selected at random then fed into the game function

**Game Function:** When the program is first opened, the instructions and current high score will be printed, with the user prompted to push the 'Enter' key (any input is accepted). The number of letters in the word is counted, and that many underscores are printed. The player must then input a letter. If the user does not enter a letter, the player will get a message based on the character they input and will be reprompted. All inputs are case insensitive.

The player's guess is compared to the letters in the word. If there is a match, the program is reset at the top of the loop, prompting them again to guess the letter. The word is also printed again, but this time with the correct letter instead of an underscore. If their guess does not match any letters in the word (i.e., they guess wrong), the underscore remains and the program subtracts one life before resetting.

- **Hint System:** This block of code is in the game mechanics function. This block will be executed if the player inputs "hint". One of the remaining letters will be scanned and printed in place of an underscore. The current number of hints will then be decreased by 1.

**Play Again Function:** The play again function will be called from the game function if the player reaches zero lives or correctly guesses a word. The player will be prompted to enter "Y" or "N" (case insensitive, and can also be "yes" and "no"). If the user continues, the program returns to the game function with the new word and their current score. If they choose to stop, the program sys.exits with a message thanking the player. 

**Scoring System Functions:** Scores are kept on a .txt using the shelve module. The high_score_open function is called during the instructions function so that the current high score can be saved. At the end of the function the file is closed. The high_score_save function is called in the play again function if the player's score is greater than the current high score to be used next time the game is played.

## Future Improvements
A potential improvement that can be made to the program is the addition of difficulty levels. One way to implement this might be to associate word length with difficult.

Another improvement could be filtering the word bank so that only basic forms of words are playable. For example, only the word "bike" could be used, but not "biking" or "biked". I think including all tenses of words make the game excessively difficult.
