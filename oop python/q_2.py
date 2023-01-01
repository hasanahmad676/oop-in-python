#write a program to create a function that will take five numbers from the user and check the number wich is divisible by 5 or 8 and also lies betwwen 1 to 100
members=[]
def function():
    for i in range(5):
        number=int(input("Enter the number: "))
        members.append(number)
        
    for k in members:
        if k%5==0 or k%8==0 and k>=1 and k<=100:
            print("The number is divisible by 5 or 8 and also lies betwwen 1 to 100: ", k)
        else:
            print("The number is not divisible by 5 or 8 and also lies betwwen 1 to 100: ", k)
print(function())

