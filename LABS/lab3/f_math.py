while True:
    from random import randint
    import random
    from calc import eval
    def genarate_quiz():
        a = randint(0,10)
        b = randint(1,10)
        error = randint(-1,1)
        op = random.choice(['+', '-', '*', '/'])
        t = eval(a,b,op) + error

        return [a,b,op,t,error]

    a,b,op,t,error = genarate_quiz()
    output = "{0} {3} {1} = {2}".format(a,b,t,op) 
    print(output)

    user_answer = input("Y/N? ").upper()
    if user_answer == "Y":
        if error == 0:
            print("Okk")
        else:
            print("Error")
    if user_answer == "N":
        if error ==0:
            print("Error")
        else:
            print("Okk")
    print("-----------")