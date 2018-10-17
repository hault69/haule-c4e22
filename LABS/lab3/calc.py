def add(x,y):
    r = x+y
    return r #cho phep r thoat ra ngoai
def eval(x,y,op):
    if op =="+":
        r = x+y
    elif op =="-":
        r = x-y
    elif op == "*":
        r = x*y
    elif op == "/":
        r = x/y
    else:
        print("Invalid operator")
    return r
# a = int(input("a: "))
# b = int(input("b: "))
# op = ("+, -, *, / : ")
# t = eval(a,b,op) #lay lai gia tri cua r
# output = "{0} {3} {1} = {2}".format(a,b,t,op) 
# print(output)