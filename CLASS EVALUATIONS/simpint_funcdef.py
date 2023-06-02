print("Good morning")
print("How are you doing? \nHow may i help you today ?")
print("My program calculates simpleinterests")
def simpint():
    p=int(input("what is the value for p"))
    r=int(input("what is the value for r"))
    t=int(input("what ia the value for t"))
    simpint=p*r*t/100
    print(f'Your value is {simpint}')
simpint()
