#make a list and search a valuew which is given by a user.
id=[2,0,1,1,5,3,1,6,0]
phn_no=[0,1,7,9,3,4,9,7,7,0,9]
lst=[1,6,0,7,7,0,9]
x=int(input("enter a value to search: "))
if x in lst:
    print("The  number you search is found in the list")
    print ("The number is found at index : " ,lst.index(x))
else:
    print(" The number you search is not found in the list")
    
    
    
