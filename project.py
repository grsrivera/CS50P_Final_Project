import random, sys
import shelve   # References used: 1) https://docs.python.org/3/library/shelve.html 2) https://www.geeksforgeeks.org/python-shelve-module/ ; used to create high score_open() and high_score_save()
from english_words import get_english_words_set     #Reference used: https://pypi.org/project/english-words/

def instructions():
    high_score=high_score_open()
    print("\nWelcome to Hangman!")
    print("These are the rules:\n1. You will be given a random word that you have to guess\n2. Guess a letter (case insensitive)\n3. If you guess correctly, the blank will be filled. If you guess wrong, you lose a life.\n   You get 7 lives for the whole game. The game is over when you lose all your lives.\n4. If you need help, type 'Hint' (case insensitive) to get a random letter filled in. You get only 3 hints the whole game.\n5. When you complete a word, you receive points in the amount of letters in that word (e.g., 'Hello' is worth 5 points).\n   Your score carries over if you choose to play again.\n\nGood luck!")
    print(f"\nThe current high score is {high_score}")
    input("\nPush 'ENTER' to start")

def high_score_open():
    file = shelve.open("high_score")
    high_score = file["high_score"]
    file.close()
    return high_score

def high_score_save(score):
    file = shelve.open("high_score")
    file["high_score"] = score
    file.close()

def get_words():
    words =  list(get_english_words_set(['web2'], alpha=True,lower=True)) #Creates 234,450 word bank
    return words

# Select word from list
def select_word(words):
    word = random.choice(words).lower()
    return word

# "Play again?" after right guess; and losing
def play_again(high_score,score):
    while True:
        x = input("Play again? (Y/N): ")
        if x.lower()=="y" or x.lower()=="yes":
            new_word = select_word(get_words())
            return True, new_word
        elif x.lower()=="n" or x.lower()=="no":
            if score>high_score:
                high_score_save(score)
                print(f"{score} is a new high score!")
            sys.exit("Thanks for playing!")
        else:
            continue

# Right/wrong guesses; Hints; Score; Lives
def game(word):
    word_letters = list(word)
    guesses = []    # Correct guesses?
    lives = 7
    score = 0
    hints = 3
    replay = False
    wrong_guesses =[]
    i=0
    high_score=high_score_open()

    while True:
        output_string_str = "x"
        wrong_guesses_str = " "
        output_string = [] # Also has purpose of clearing out string on each iteration so it doesn't create a long list


        if i==0:    # Show blanks for first run
            initial_blanks = "_ " * len(word)
            print(f"\n{initial_blanks}")

        guess = input(f"\nGuess: ").lower()

        if guess in guesses and guess!="hint":    # No repeat guesses
            print("\nAlready tried!")
            continue

        if guess.isalpha() == False:
            print("Letters only!")
            #break   # Only use for pytesting
            continue

        if len(guess)>1 and guess!="hint":
            print("\nOne letter at a time!")
            continue

        if guess == "hint":     # Hint system. After completing goes to other blocks
            if hints<=0:
                print("\nOut of hints!")
                continue
            hints = hints - 1
            # Remove guessed letters from possible hints
            possible_hints = word_letters.copy()

            for letter in word_letters:
                if letter in guesses:
                    possible_hints.remove(letter)
            letter_hint = random.choice(possible_hints)       # Choose random letter not already guessed

            guess = letter_hint     # So it gets fed into "if guess in word" and prints

        guesses.append(guess)

        for letter in word_letters: # Check to see if guess is right
            if letter in guesses:
                output_string.append(f"{letter.upper()} ")     # Add letter to list if right, capitalized
            else:
                output_string.append("_ ")      # Add underscore to list if letter still not guessed

        output_string_str = "".join(output_string).replace("_","").replace(" ","")      # Made this str instead of joining list because "word" is string

        if guess not in word and guess!="hint":

            wrong_guesses.append(guess.upper())
            wrong_guesses_str = ", ".join(wrong_guesses)
            lives=lives-1
            print("\nLetter not in word")
            print(f"\nScore: {score}        Lives: {lives}        Hints: {hints}        Wrong Letters: {wrong_guesses_str}\n")
            print("".join(output_string))

        if lives == 0:        # End game if all lives lost
            print(f"\nScore: {score}        Lives: {lives}        Hints: {hints}        Wrong Letters: {wrong_guesses_str}\n")
            print(f"Thanks for playing!\nThe answer is '{word.upper()}'.\n")
            replay, word = play_again(high_score,score)
            if replay == True:
                score=0
                lives=3
                hints=3
                guesses = []
                wrong_guesses = []
                i=0
                word = word
                word_letters = list(word)
                wrong_guesses_str = " "
                print(f"\n\n\n\n\n\n\n\nScore: {score}        Lives: {lives}        Hints: {hints}        Wrong Letters: {wrong_guesses_str}\n")
                continue

        if guess in word:     # Correct guess
            wrong_guesses_str = ", ".join(wrong_guesses)
            print(f"\nScore: {score}        Lives: {lives}        Hints: {hints}        Wrong Letters: {wrong_guesses_str}\n")
            print("".join(output_string))


        if output_string_str == word.upper():   # Next word if complete and update score
            score = score + len(output_string_str)
            print(f"\nCorrect!")
            print(f"\n\n\n\n\n\nScore: {score}        Lives: {lives}        Hints: {hints}        Wrong Letters: {wrong_guesses_str}\n")
            replay, word = play_again(high_score,score)
            if replay == True:      # Reset all variables
                guesses = []
                wrong_guesses = []
                i=0
                word = word
                word_letters = list(word)
                #possible_hints = []
                continue

        i=i+1   # Only used to identify first iteration

def main():
    instructions()
    game((select_word(get_words())))



if __name__ == "__main__":
    main()
