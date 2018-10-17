x = int(input("nhap x: "))
y = int(input("nhap y: "))
op = input("Op (+,-,*,/): ")
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
print(x,op,y,"= ",r)