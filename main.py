import tingbot
from tingbot import *

import random

' figure out about global variables'

state = {'space': [310,230], 'status' : 0, 'level': 30, 'multiplier':10, 'direction': [1,0], 'snake': [0,0], 'food': [200,60], 'counter': 0 }


def generate_food():
    state['food'][0] = random.randint(0, 29) * 10 + 10
    state['food'][1] = random.randint(0, 19) * 10 + 30
    while state['food'] in state['snake']:
        state['food'][0] = random.randint(0, 29) * 10 + 10
        state['food'][1] = random.randint(0, 19) * 10 + 30

def make_move():
    new_position = [state['snake'][0][0]+state['direction'][0]*state['multiplier'],state['snake'][0][1]+state['direction'][1]*state['multiplier']]
    if new_position == state['food']:
        state['snake'].insert(0,[state['food'][0],state['food'][1]]) 
        generate_food()
    elif new_position[0] == 0 or new_position[0] == state['space'][0] or new_position[1] == 20 or new_position[1] == state['space'][1]:
        state['status'] = 0
    else:
        x = len(state['snake']) - 1
        while x > 0:
            state['snake'][x] = state['snake'][x-1]
            x+= -1
        state['snake'][0] = new_position
        
@left_button.press
def on_left_pressed():
    if state['direction'][0] == 0:
        state['direction'] = [-1,0]

@right_button.press
def on_right_pressed():
    if state['direction'][0] == 0:
        state['direction'] = [1,0]

@midleft_button.press
def on_up_pressed():
    if state['direction'][1] == 0:
        state['direction'] = [0,-1]

@midright_button.press
def on_down_pressed():
    if state['direction'][1] == 0:
        state['direction'] = [0,1]

        
@touch()
def on_touch(xy):
    if state['status'] == 0:
        start_game()


def update_screen():
    screen.fill(color='blue')
    screen.rectangle(xy=(10, 30), size=(300,200), color='green', align='topleft')
    for each in state['snake']:
        screen.rectangle(xy=(each[0], each[1]), size=(10,10), color='white', align='topleft')
    screen.rectangle(xy=(state['food'][0], state['food'][1]), size=(10,10), color='red', align='topleft') 


def start_game():
    screen.fill(color='blue')
    screen.rectangle(xy=(10, 30), size=(300,200), color='green', align='topleft')
    state['status'] = 1
    state['snake'] = [[100,100],[90,100],[80,100],[70,100]]
    state['direction'] = [1,0]
    generate_food()
    
    

@every(seconds=1.0/30)
def loop():
    
    if state['status'] == 0:
        state['counter'] = 0
        screen.fill(color='black')
        screen.text('Start game - press anywhere!', xy=(20,20), align='topleft', max_width=280)
        screen.text('Controls: Left to go left; middle left - up; middle right - down; right - right', font_size=12, xy=(20, 170), align='topleft', max_width=280)
        
    else:
        if state['counter'] < state['level']:
            state['counter'] += 1
        else:
            make_move()
            state['counter'] = 0
            update_screen()
        

tingbot.run()
