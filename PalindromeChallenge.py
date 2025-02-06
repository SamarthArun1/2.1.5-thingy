from random import randint

grid = [
    [0, 0, 1, 0, 0],
    [1, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 2]
]

coords = [0, 0, 180]  # [row, col, direction]

# Function to make a random turn (changing direction)
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

# Function to move the robot based on current direction
def randomsolving():
    if coords[2] == 90:  # Facing right
        if coords[1] + 1 < len(grid[0]) and grid[coords[0]][coords[1] + 1] != 1:  # Check right
            coords[1] = coords[1] + 1
        else:
            print("Path blocked or out of bounds (right), turning")
            randomturning()
    elif coords[2] == 180:  # Facing down
        if coords[0] + 1 < len(grid) and grid[coords[0] + 1][coords[1]] != 1:  # Check down
            coords[0] = coords[0] + 1
        else:
            print("Path blocked or out of bounds (down), turning")
            randomturning()
    elif coords[2] == 270:  # Facing left
        if coords[1] - 1 >= 0 and grid[coords[0]][coords[1] - 1] != 1:  # Check left
            coords[1] = coords[1] - 1
        else:
            print("Path blocked or out of bounds (left), turning")
            randomturning()
    elif coords[2] == 0:  # Facing up
        if coords[0] - 1 >= 0 and grid[coords[0] - 1][coords[1]] != 1:  # Check up
            coords[0] = coords[0] - 1
        else:
            print("Path blocked or out of bounds (up), turning")
            randomturning()

# Initialize move count
count = 0

# Ensure robot doesn't go out of bounds
while 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0]) and grid[coords[0]][coords[1]] != 2:
    randomsolving()  # Move robot
    count += 1  # Increment move counter
    print(f"Move {count}: Robot at position {coords[0]}, {coords[1]}")

    # Fail-safe: If robot moves out of bounds, break the loop
    if not (0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])):
        print("Robot went out of bounds. Exiting.")
        break

print(f"Reached end in {count} moves" if grid[coords[0]][coords[1]] == 2 else "Failed to reach the end.")
