mul=1
value=1

while value<13:
    mul = 1 #initializes the variable from mul 20 to 1
    while mul<20:
        print(f"{value} x {mul}={mul*value}")
        mul+=1
    print(f'\n\n')
    value+=1