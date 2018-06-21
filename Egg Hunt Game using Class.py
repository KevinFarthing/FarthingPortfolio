from random import choice
from random import shuffle
from random import randint
# from IPython.display import clear_output

class EggGame:
    def __init__(self):
        self.grid = self.board_gen()
        self.hero = [4,2]
        self.eggs = self.egg_hider()
        self.monster = self.monster_gen()
        self.door = self.door_gen()      
        self.eggs_found = 0  

    def board_gen(self):
        grid = []
        for i in range(5):
            grid_row = []
            for j in range(5):
                grid_row.append((i,j))
            grid.append(grid_row)
        return grid
        
    def print_board(self):
        for row in range(5):
            for col in range(5):
                if self.grid[row][col] in self.eggs:
                    print("[0]", end="")
                elif self.grid[row][col] == self.monster:
                    print("[X]", end="")
                elif self.grid[row][col]== self.door:
                    print("[D]", end="")
                elif self.grid[row][col] == tuple(self.hero):
                    print("[H]", end="")
                else:
                    print(f"[_]", end="")
            print('\n')



    def egg_hider(self):
        eggs = []
        for egg in range(3):
            eggs.append((randint(0,4),randint(0,4)))
        return eggs

    def monster_gen(self):
        monster = (randint(0,4),randint(0,4))
        while monster in self.eggs or monster == self.hero:
            monster = (randint(0,4),randint(0,4))
        return monster

    def door_gen(self):
        while True:
            door = [choice([0,4]),randint(0,4)]
            shuffle(door)
            door = tuple(door)
            if door != self.monster and door not in self.eggs:
                return door

    def end_check(self):
        game_over = False
        if self.eggs == [] and tuple(self.hero) == self.door:
            self.print_board()
            print("You have found all the eggs and made it to the door!")
            print("You Win!")
            game_over = True

        if tuple(self.hero) == self.monster:
            self.print_board()
            print("You have been devoured by a Grue")
            print("Game over.")
            game_over = True
        return game_over

    def egg_check(self):
        if tuple(self.hero) in self.eggs:
            print("Good Job, you found an egg!")
            self.eggs_found += 1
            print(f"You have {self.eggs_found} eggs!")
            self.eggs.remove(tuple(self.hero))
            if self.eggs == []:
                print("You found all the eggs!")
        # return eggs, eggs_found

    def get_move(self):
        inside_boundaries = True
        move = input("Up [w], Down [s] Left [a] or Right [d]: ").lower()
        while move not in "wasd":
            print("Please enter a valid move")
            move = input("Up [w], Down [s] Left [a] or Right [d]: ").lower()
        
        while inside_boundaries:
            if move == "w" and self.hero[0] != 0:
                self.hero[0] -= 1
                break
            elif move == "a" and self.hero[1] != 0:
                self.hero[1] -= 1
                break
            elif move == "s" and self.hero[0] != 4:
                self.hero[0] += 1
                break
            elif move == "d" and self.hero[1] != 4:
                self.hero[1] += 1
                break
            else:
                print("That's a wall!")
                inside_boundaries = False
        # return hero

    def main(self):
        while not self.end_check():
            self.print_board()
            self.get_move()
            self.egg_check()

EggGame().main()