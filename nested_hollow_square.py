a = int(input())
b = int(input())

if b >= a or a > 20 or b > 20 or a < 1 or b < 1:
    print("Wrong order!")

elif ((a-b) % 2) != 0:
    print("Wrong difference!")

else:
    c = int((a-b)*0.5)
    for i in range (c):
        print("* " * a)
    
    for i in range (b):
        print("* " * c, "  " * (b-1), "* " * c)
    
    for i in range (c):
        print("* " * a)
