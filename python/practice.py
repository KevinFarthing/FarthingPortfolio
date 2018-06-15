# from IPython.display import clear_output
from random import randint
from modules import word_list

class Hangman:
    def __init__(self, word="", lives=6, status=[],wrong=[]):
        self.lives = lives
        self.word = word
        self.status = status
        self.wrong = wrong

    # def word_select():
    #         return word_list[randint(0,len(word_list)-1)]

    def guess_check(self):
        guess = input("Guess a letter: ")
        while len(guess)>1:
            guess = input("Guess ONE letter: ").lower()
        if guess in self.word.lower():
            print(f"Awesome! {guess} is in the word!")
            for i in range(len(self.word)):
                if self.word[i].lower() == guess:
                    self.status[i] = self.word[i]
        else:
            self.lives -= 1
            print(f"Sorry, {guess} was not in the word.")
            self.wrong.append(guess)
    #     print_status(status,lives,wrong)
        # return status, lives, wrong

    def print_status(self):
        # clear_output()
        print("***************")
        print(f"Lives: {self.lives}")
        print(f"Past Guesses: ", end="")
        print(" ".join(self.wrong))
        print(" ".join(self.status))

    def game_function(self):
        self.lives = 6
        self.wrong = []
        while self.lives != 0:
            self.print_status()
            self.guess_check()
            if "_" not in self.status:
                print("You Win!")
                print(f"The word was {self.word}")
                return
        print(f"Game Over! The correct word was {self.word}!")

    def main(self):
        while True:
            self.word = word_list[randint(0,len(word_list)-1)]
            self.status = list("_"*len(self.word))
            self.game_function()
            cont = input("Would you like to play again? y/n ").lower()
            if cont != "y":
                print("Thanks for playing!")
                break

              
# game = Hangman()
# game.main()

Hangman().main()