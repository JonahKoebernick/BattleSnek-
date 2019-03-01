
import numpy as np
def calculate_move(board_matrix,head,height):
    directions = {'up':0, 'down':0, 'left':0, 'right':0}
    # Check up
    if head["y"] - 1 < 0 or board_matrix[head["y"] - 1,head["x"]] == 1:
        directions["up"] = 100
    else:
        directions["up"] = sum(board_matrix, head["x"], head["y"] - 1)

    # Check down
    if head["y"] + 1 >= (height - 1) or board_matrix[head["y"] + 1 ,head["x"]] == 1:
        directions["down"] = 100
    else:
        directions["down"] = sum(board_matrix, head["x"], head["y"] + 1)

    # Check Left
    if head["x"] - 1 < 0 or board_matrix[head["y"] ,head["x"] - 1] == 1:
        directions["left"] = 100
    else:
        directions["left"] = sum(board_matrix, head["x"] - 1, head["y"])

    # check right
    if head["x"] + 1 >= (height - 1) or board_matrix[head["y"] ,head["x"] + 1] == 1:
        directions["right"] = 100
    else:
        directions["right"] = sum(board_matrix, head["x"] + 1, head["y"])

    return min(directions, key=lambda k: directions[k])

def sum(matrix,x,y):
    sum =0
    sum += matrix[y, x-1]
    sum += matrix[y, x+1]
    sum += matrix[y-1, x]
    sum += matrix[y+1, x]
    return sum

