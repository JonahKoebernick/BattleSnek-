
import numpy as np
UNOCCUPIED = 0
OCCUPIED   = 1
FOOD       = -10
HEAD       = 10
HEALTHLIM = 50
game_state = ""

def calculate_move(board_matrix, game_state):
    set_game_state(game_state)
    height = game_state["board"]["height"]
    head= game_state['you']["body"][0]
    health = game_state['you']["health"]
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
        if matrix[y, x-1]  is HEAD:
            if is_bigger(game_state['you']["body"], get_snek(x-1, y, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
             sum += matrix[y, x-1]
    else:
        sum += 1
    if (x+1) < height:
        if matrix[y, x+1]  is HEAD:
            if is_bigger(game_state['you']["body"], get_snek(x+1, y, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
            sum += matrix[y, x+1]
    else:
        sum += 1
    if (y-1) >= 0:
        if matrix[y-1, x]  is HEAD:
            if is_bigger(game_state['you']["body"], get_snek(x, y-1, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
            sum += matrix[y-1, x]
    else:
        sum += 1
    if (y+1) < height:
        if matrix[y+1, x]  is HEAD:
            if is_bigger(game_state['you'], get_snek(x, y+1, get_game_state())):
                sum -= HEAD
            else:
                sum += HEAD
        else:
            sum += matrix[y+1, x]
    else:
        sum += 1

    if matrix[y,x] == FOOD and sum <12 and health < HEALTHLIM:
        return -100
    return sum


def get_snek(x, y, game_state):
    for snek in game_state["board"]["snakes"]:
        if x in snek["body"]["x"] and y in snek["body"]["y"]:
            return snek

def is_bigger(snek1, snek2):
    if len(snek1["body"]["x"]) > len(snek2["body"]["x"]):
        return true
    return false
    
def set_game_state(new_game_state):
    game_state = new_game_state

def get_game_State():
    return game_state