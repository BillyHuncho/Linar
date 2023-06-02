worker1=int(input("what is your income"))
worker2=int(input("what is your income"))
worker3=int(input("what is your income"))
worker4=int(input("what is your income"))
worker5=int(input("what is your income"))
total=worker1+worker2+worker2+worker3+worker4+worker5
balance=250000-total
print(balance)
statement="Hello employer the total expected income from your worker is "+str(total) + "and the outstanding balance is "+str(balance)
print(statement)