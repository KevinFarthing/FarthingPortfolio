# from IPython.display import clear_output
from random import randint
from modules import word_list

def word_select():
        return word_list[randint(0,len(word_list)-1)]

def guess_check(word, status, lives,wrong):
    guess = input("Guess a letter: ")
    while len(guess)>1:
        guess = input("Guess ONE letter: ").lower()
    if guess in word.lower():
        print(f"Awesome! {guess} is in the word!")
        for i in range(len(word)):
            if word[i].lower() == guess:
                status[i] = word[i]
    else:
        lives -= 1
        print(f"Sorry, {guess} was not in the word.")
        wrong.append(guess)
#     print_status(status,lives,wrong)
    return word, status, lives, wrong

def print_status(status,lives,wrong):
    # clear_output()
    print("***************")
    print(f"Lives: {lives}")
    print(f"Past Guesses: ", end="")
    print(" ".join(wrong))
    print(" ".join(status))

def game_function():
    word = word_select()
    lives = 6
    wrong = []
    status = list("_"*len(word))
    while lives != 0:
        print_status(status,lives,wrong)
        word, status, lives, wrong = guess_check(word, status, lives, wrong)
        if "_" not in status:
            print("You Win!")
            print(f"The word was {word}")
            return
    print(f"Game Over! The correct word was {word}!")

def main():
    while True:
        game_function()
        cont = input("Would you like to play again? y/n ").lower()
        if cont != "y":
            print("Thanks for playing!")
            break


              
main()