from random import choice
from random import shuffle
from random import randint
from IPython.display import clear_output

def board_gen():
    grid = []
    for i in range(5):
        grid_row = []
        for j in range(5):
            grid_row.append((i,j))
        grid.append(grid_row)
    return grid
    
def print_board(eggs, monster, door, hero, grid):
    for row in range(5):
        for col in range(5):
            if grid[row][col] in eggs:
                print("[0]", end="")
            elif grid[row][col] == monster:
                print("[X]", end="")
            elif grid[row][col]== door:
                print("[D]", end="")
            elif grid[row][col] == tuple(hero):
                print("[H]", end="")
            else:
                print(f"[_]", end="")
        print('\n')



def egg_hider():
    eggs = []
    for egg in range(3):
        eggs.append((randint(0,4),randint(0,4)))
    return eggs

def monster_gen(eggs, hero):
    monster = (randint(0,4),randint(0,4))
    while monster in eggs or monster == hero:
        monster = (randint(0,4),randint(0,4))
    return monster

def door_gen(eggs, hero, monster):
    while True:
        door = [choice([0,4]),randint(0,4)]
        shuffle(door)
        door = tuple(door)
        if door != monster and door not in eggs:
            return door

def end_check(eggs, monster, door, hero, grid):
    game_over = False
    if eggs == [] and tuple(hero) == door:
        print_board(eggs, monster, door, hero, grid)
        print("You have found all the eggs and made it to the door!")
        print("You Win!")
        game_over = True

    if tuple(hero) == monster:
        print_board(eggs, monster, door, hero, grid)
        print("You have been devoured by a Grue")
        print("Game over.")
        game_over = True
    return game_over

def egg_check(hero, eggs, eggs_found):
    if tuple(hero) in eggs:
        print("Good Job, you found an egg!")
        eggs_found += 1
        print(f"You have {eggs_found} eggs!")
        eggs.remove(tuple(hero))
        if eggs == []:
            print("You found all the eggs!")
    return eggs, eggs_found

def get_move(hero):
    inside_boundaries = True
    move = input("Up [w], Down [s] Left [a] or Right [d]: ").lower()
    while move not in "wasd":
        print("Please enter a valid move")
        move = input("Up [w], Down [s] Left [a] or Right [d]: ").lower()
    
    while inside_boundaries:
        if move == "w" and hero[0] != 0:
            hero[0] -= 1
            break
        elif move == "a" and hero[1] != 0:
            hero[1] -= 1
            break
        elif move == "s" and hero[0] != 4:
            hero[0] += 1
            break
        elif move == "d" and hero[1] != 4:
            hero[1] += 1
            break
        else:
            print("That's a wall!")
            inside_boundaries = False
    return hero

def main():
    grid = board_gen()
    hero = [4,2]
    eggs = egg_hider()
    monster = monster_gen(eggs, hero)
    door = door_gen(eggs, hero, monster)      
    eggs_found = 0  

    while not end_check(eggs, monster, door, hero, grid):
        clear_output()
        print_board(eggs, monster, door, hero, grid)

        hero = get_move(hero)

        
        eggs, eggs_found = egg_check(hero, eggs, eggs_found)



main()