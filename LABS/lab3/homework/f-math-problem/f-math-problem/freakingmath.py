from random import *
import random
from calc import eval
def generate_quiz():
    # Hint: Return [x, y, op, result]
    x = randint(0,10)
    y = randint(1,10)
    op = random.choice(['+', '-', '*', '/'])
    result = eval(x,y,op) + randint(-1,1)
    return [x,y,op,result]
def check_answer(x, y, op, result, user_choice):
    if user_choice == True:
        if result == eval(x,y,op):
            return True
        else:
            return False
    else:
        if result == eval(x,y,op):
            return False
        else:
            return True