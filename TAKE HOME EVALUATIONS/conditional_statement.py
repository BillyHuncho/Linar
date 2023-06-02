#A script that will run with the users input using the IF,ELIF AND ELSE conditional statement
Score=int(input("What is your score ? "))
if Score <=39 and Score >=0:
    print("Fail")
elif Score <=49 and Score >=40:
    print("Poor")
elif Score <=59 and Score  >=50:
    print("Pass")
elif Score <=69 and Score >=60:
    print("Good")
elif Score <=100 and Score >=70:
    print("Excellent")
else:
    print("Check with your tutor")