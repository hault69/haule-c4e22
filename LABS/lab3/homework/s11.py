def is_inside(a, b):
    if b[0] <= a[0] <= (b[0]+b[2]) and b[1] <= a[1] <= (b[1]+b[3]):
        # print("trong")
        return True
    else:
        # print("ngoài")
        return False
# a = [100000, 120]
# b= [140, 60, 100, 200]
# is_inside(a,b)


