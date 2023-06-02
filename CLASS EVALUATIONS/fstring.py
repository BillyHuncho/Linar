#fstring of conversion
print("Good morning")

print("how can i help you today")

print("welcome to my program where you can convert from kg to g\n g to kg \n m to cm \n cm to m \n ft to inc \n inc to ft ")

unit=int(input("what unit are you working with ?\n for kg to g press 1\n for g to kg press 2\n for m to cm press 3\n for cm to m press 4\n for inc to ft press 5\n for ft to inc press 6? \n "))

value=int(input("what is the value ?"))
def kg_to_g (value):
    print(f"Your converted value for kg to g is {value*1000}" )


def g_to_kg (value): 
    print(f"Your converted value is {value/1000}" )


def m_to_cm (value):
    print(f"Your converted value is {value*100}")


def cm_to_m(value):
    print(f"Your converteed value is {value/100}")


def ft_to_inc(value):
    print(f"Your converted value is {value*12}")


def inc_to_ft(value):
    print(f"Your converted value is {value/12}")     



if unit==1:
    kg_to_g(value)
elif unit==2:
    g_to_kg(value)
elif unit==3:
    m_to_cm(value)
elif unit==4:
    cm_to_m(value)
elif unit==5:
    ft_to_inc(value)
elif unit==6:
    inc_to_ft(value)
else:
    print("Input a valid unit")




