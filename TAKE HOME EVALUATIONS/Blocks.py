#code to calculate the number of blocks required to build a room
def Areaofroom():
    wall1=int(input("what is the lenght of wall 1 ?"))
    wall2=int(input("what is the length of wall 2 ?"))
    wall3=int(input("what is the length of wall 3 ?"))
    wall4=int(input("what is the length of wall 4 ?"))
    TotalLength=wall1+wall2+wall3+wall4
    Areaofroom=TotalLength*10
    return(Areaofroom)
def Areaofoneblock():
    length=10
    height=0.5
    Areaofoneblock=length*height
    return(Areaofoneblock)
print('The number of blocks required is' +str(Areaofroom()/Areaofoneblock()))