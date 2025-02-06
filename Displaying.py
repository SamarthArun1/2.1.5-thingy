from random import randint

grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2]
]

coords = [0, 0, 0]
count = 0

def randomturning():
    turn = randint(1, 2)
    if turn == 1:
        if coords[2] == 270:
            coords[2] = 0
        else:
            coords[2] = coords[2] + 90
    else:
        if coords[2] == 0:
            coords[2] = 270
        else:
            coords[2] = coords[2] - 90

def randomsolving():
    if coords[2] == 90:  
        if coords[1] + 1 < len(grid[0]) and grid[coords[0]][coords[1] + 1] == 1: 
            print("path is blocked, turning")
            randomturning()
        else:
            print("moving forward")
            coords[1] = coords[1] + 1
    elif coords[2] == 180:
        if coords[0] + 1 < len(grid) and grid[coords[0] + 1][coords[1]] == 1:  
            print("path is blocked, turning")
            randomturning()
        else:
            print("moving forward")
            coords[0] = coords[0] + 1
    elif coords[2] == 270:
        if coords[1] - 1 >= 0 and grid[coords[0]][coords[1] - 1] == 1:  
            print("path is blocked, turning")
            randomturning()
        elif coords[1] - 1 < 0:  
            print("can't move left, turning")
            randomturning()
        else:
            print("moving forward")
            coords[1] = coords[1] - 1
    elif coords[2] == 0: 
        if coords[0] - 1 >= 0 and grid[coords[0] - 1][coords[1]] == 1:
            print("path is blocked, turning")
            randomturning()
        elif coords[0] - 1 < 0: 
            print("can't move up, turning")
            randomturning()
        else:
            print("moving forward")
            coords[0] = coords[0] - 1
    else:
        print("facing a different direction")
while grid[coords[0]][coords[1]] != 2:
    randomsolving()
    count = count + 1
print(f"reached end in {count} moves")

