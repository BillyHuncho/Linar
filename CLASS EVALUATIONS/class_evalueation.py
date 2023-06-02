student1=int(input("how much has student1 paid for school fee"))
student2=int(input("how much has student2 paid for school fee"))
student3=int(input("how much has student3 paid for school fee"))
student4=int(input("how much has student4 paid  for school fee"))
student5=int(input("how much has student5 paidfor school fee"))
total=student1+student2+student2+student3+student4+student5
expectedincome=input("what is your expected income?")
balance= 25000-total
print(expectedincome)
statement="Hello employer the total expected income from your class is "+str(expectedincome) + "and the outstanding balance is "+str(balance)
print(statement) 