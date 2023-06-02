st_first_name=[]
st_last_name = []

while len(st_first_name) <= 5:    
    fname=input("What is your  firstname ?\n")
    lname=input("What is your lastname ?\n")
    st_first_name.append(fname)
    st_last_name.append(lname)
    print("Data Successfully uploaded\n\n")


for fname,lname in zip(st_first_name,st_last_name):
    print(f'Welcome {fname} from the family of {lname}')