#conversion of units
print("Good morning")

print("how can i help you today")

print("welcome to my program where you can convert from kg to g\n g to kg \n m to cm \n cm to m \n ft to inc \n inc to ft ")

unit=int(input("what unit are you working with ?\n for kg to g press 1\n for g to kg press 2\n for m to cm press 3\n for cm to m press 4\n for inc to ft press 5\n for ft to inc press 6? \n "))


value=int(input("what is the value ?"))
def kg_to_g (value):
    print("Your converted value for kg_to_g is " +str(value*1000))


def g_to_kg (value): 
    print("Your converted value for g_to_kg is " +str(value/1000))


def m_to_cm (value):
    print("Your converted value for m_to_cm is "+ str(value*100))


def cm_to_m(value):
    print("Your converted value for cm_to_m  is " + str(value/100))


def ft_to_inc(value):
    print("Your converted value for ft_to_inc is " + str(value*12))


def inc_to_ft(value):
    print("Your converted value for inc_to_ft is " + str(value/12))     



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


