#write a program of the almighty formular
from math import sqrt
a=int(input("what is the first variable ? "))
b=int(input("what is the second variable ?"))
c=int(input("what is the third variable ?"))
d=b*b-4*a*c
X=(-b + sqrt(d)) / (2*a)
Y=(-b - sqrt(d)) / (2*a)
print(X)
print(Y)