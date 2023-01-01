'''ch=input("Enter the number of characters: ")
vaowal="a,e,i,o,u,A,E,I,O,U"
if ch in vaowal:
    print("Vowel")
else:
    print("Consonant")'''
    
#find the largest number in the given three numbers
'''num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
num3=int(input("Enter the third number: ")) 
if num1>num2 and num1>num3:
    print("The largest number is: ",num1)
elif num2>num1 and num2>num3:
    print("The largest number is: ",num2)
else:
    print("The largest number is: ",num3)'''
    
'''#create a number grade system
number=int(input("Enter the number: "))
if number>=90:
    print("A")
elif number>=80:
    print("B")
elif number>=75:
    print("C")
elif number>=70:
    print("D")
else:
    print("F")'''

#find the sum of the given numbers uding while loop
'''number=int(input("Enter the number: "))
sum=0
i=1
while i<=number:
    sum=sum+i
    i=i+1
print("The sum of the numbers is: ",sum)'''
#print paatern of given number 
'''n=int(input("Enter the number: "))
for i in range(1,n+1):
    for j in range(1,i+1):
        print("j",end=" ")
    print()'''


#calculate truangle area
'''class Triangle:
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def area(self):
        return self.base*self.height/2

t=Triangle(10,20)
print(t.area())'''

#multilevel inheritance
class A:
    def display1(self):
        print("In class A")
class B(A):
    def display2(self):
        print("In class B")
class C(B):
    def display3(self):
        print("In class C")
        
c=C()
c.display1()
c.display2()
c.display3()