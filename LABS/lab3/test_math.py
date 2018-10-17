from random import randint
import random
while True:
    x = randint(0,10)
    y = randint(1,10)
    error = randint(-1,1)
    calc = ['+','-','*','/']
    a = random.choice(calc)
    if a =="+":
        r = x+y+error
        output = "{0} + {1} = {2}".format(x,y,r)
        print(output)
        user_answer = input("Y/N? ")
        if user_answer == "y":
            if r == x+y:
                print("Yahh")
            else:
                print("error!!!")
        if user_answer =="n":
            if r == x+y:
                print("error!!!")
            else:
                print("Yahh")
    elif a == "-":
        r = x-y+error
        output = "{0} - {1} = {2}".format(x,y,r)
        print(output)
        user_answer = input("Y/N? ")
        if user_answer == "y":
            if r == x-y:
                print("Yahh")
            else:
                print("error!!!")
        if user_answer =="n":
            if r == x-y:
                print("error!!!")
            else:
                print("Yahh")
    elif a == "*":
        r = x*y+error
        output = "{0} * {1} = {2}".format(x,y,r)
        print(output)
        user_answer = input("Y/N? ")
        if user_answer == "y":
            if r == x*y:
                print("Yahh")
            else:
                print("error!!!")
        if user_answer =="n":
            if r == x*y:
                print("error!!!")
            else:
                print("Yahh")
    elif a == "/":
        r = x/y+error
        output = "{0} / {1} = {2}".format(x,y,r)
        print(output)
        user_answer = input("Y/N? ")
        if user_answer == "y":
            if r == x/y:
                print("Yahh")
            else:
                print("error!!!")
        if user_answer =="n":
            if r == x/y:
                print("error!!!")
            else:
                print("Yahh")
    print("*********************************")