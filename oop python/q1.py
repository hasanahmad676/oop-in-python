course = input("Type of ciurse (Lab of Theory)  ") 
t = int (input("Number of classes take by the teacher "))
s = int(input("Number of classes attented by a student "))

if(course == "theory"):
    if((s/t)*100)>=65:
        print("Allowed for the final exam")
    else:
        print("Not allowed for the final exam")
elif(course == "lab"):
    if((s/t)*100)>=70:
        print("Allowed for the final exam")
    else:
        print("Not allowed for the final exam")
































































































