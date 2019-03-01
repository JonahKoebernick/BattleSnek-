import json
import os
import random
import bottle

from api import ping_response, start_response, move_response, end_response

@bottle.route('/')
def index():
    return bottle.static_file('index.html', root='../static/')

@bottle.route('/static/<path:path>')
def static(path):
    return bottle.static_file(path, root='../static/')


@bottle.post('/ping')
def ping():
    return ping_response()


@bottle.post('/start')
def start():
    game_state = bottle.request.json

    color = "#00FF00"

    return start_response(color)


@bottle.post('/move')
def move():
    game_state = bottle.request.json
    height = game_state["board"]["height"]
    board_matrix = [[0] * height for i in range(height)]
    body = game_state["you"]["body"]
    head = game_state["you"]["body"][0]
    for i in range(len(body)):
        board_matrix[body[i]["x"]][body[i]["y"]]=1
    directions = {'up':0, 'down':0, 'left':0, 'right':0}

    #Check up
    if  head["y"]-1 < 0 or board_matrix[head["x"]][head["y"]-1]==1:
         directions["up"]=100
    else:
        directions["up"] = sum(board_matrix,head["x"],head["y"]-1)

    #Check down
    if head["y"]+1 >= (height-1)  or board_matrix[head["x"]][head["y"]+1]==1:
        directions["down"]=100
    else:
        directions["down"] = sum(board_matrix, head["x"], head["y"] +1)

    #Check Left
    if  head["x"]-1 < 0 or board_matrix[head["x"]-1][head["y"]]==1:
        directions["left"]=100
    else:
        directions["left"] = sum(board_matrix, head["x"]-1, head["y"] )

    #check right
    if head["x"]+1 > (height-1) or  board_matrix[head["x"]+1][head["y"]] == 1:
        directions["right"]=100
    else:
        directions["right"] = sum(board_matrix, head["x"]+1, head["y"] )



    print(game_state)
    print(board_matrix)

    return move_response(min(directions, key=lambda k: directions[k]))

def sum(matrix,x,y):
    sum =0
    sum += matrix[x-1][y]
    sum += matrix[x+1][y]
    sum += matrix[x][y-1]
    sum += matrix[x][y+1]
    return sum

@bottle.post('/end')
def end():
    game_state = bottle.request.json

    return end_response()

# Expose WSGI app (so gunicorn can find it)
application = bottle.default_app()

if __name__ == '__main__':
    bottle.run(
        application,
        host=os.getenv('IP', '127.0.0.1'),
        port=os.getenv('PORT', '49121'),
        debug=os.getenv('DEBUG', True)
    )
