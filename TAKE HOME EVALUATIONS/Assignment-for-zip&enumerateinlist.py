Names='Bobby','Naomi','chris','Blair','Tom'
Subjects='Maths','English','Coding','Civic','Edu'
Marks=94,85,99,73,89
#To use the enumerate(),zip() to iterate the list we have 
for s,(Names,Subjects,Marks) in enumerate(zip(Names,Subjects,Marks)):
    print(s,Names,Subjects,Marks)