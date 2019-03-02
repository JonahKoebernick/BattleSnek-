
import numpy as np
UNOCCUPIED = 0
OCCUPIED   = 1
FOOD       = -10
HEAD       = 1
HEALTHLIM = 30

def calculate_move(board_matrix,us,height):
    head= us["body"][0]
    health = us["health"]
    directions = {'up': 0, 'down': 0, 'left': 0, 'right': 0}
    # Check up
    if head["y"] - 1 < 0 or board_matrix[head["y"] - 1,head["x"]] == OCCUPIED :
        directions["up"] = 1000
    else:
        directions["up"] = sum(board_matrix, head["x"], head["y"] - 1,height, health)

    # Check down
    if head["y"] + 1 > (height - 1) or board_matrix[head["y"] + 1 ,head["x"]] == OCCUPIED :
        directions["down"] = 1000
    else:
        directions["down"] = sum(board_matrix, head["x"], head["y"] + 1,height, health)

    # Check Left
    if head["x"] - 1 < 0 or board_matrix[head["y"] ,head["x"] - 1] == OCCUPIED :
        directions["left"] = 1000
    else:
        directions["left"] = sum(board_matrix, head["x"] - 1, head["y"],height, health)

    # check right
    if head["x"] + 1 > (height - 1) or board_matrix[head["y"] ,head["x"] + 1] == OCCUPIED :
        directions["right"] = 1000
    else:
        directions["right"] = sum(board_matrix, head["x"] + 1, head["y"],height, health)

    return min(directions, key=lambda k: directions[k])

def sum(matrix,x,y,height, health):
    sum = 0

    if  (x-1) >= 0:
        sum += matrix[y, x-1]
    if (x + 1) < height:
        sum += matrix[y, x+1]
    if (y-1) >= 0:
        sum += matrix[y-1, x]
    if (y+1) < height:
        sum += matrix[y+1, x]

    if matrix[y,x] == FOOD and sum <12 and health < HEALTHLIM:
        return -100
    return sum

