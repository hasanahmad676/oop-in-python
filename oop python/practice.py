###Write a program to print the roll number and average marks of 8 students in three subjects (each out of 100). 
# The marks are entered by user.###

n=int(input("Enter the number of the  students: "))
for i in range(n):
      name=input("Enter the id of the student : " )
      sub_1=int(input("Enter the sub_1 number: ")) 
      sub_2=int(input("Enter the sub_2 number: "))
      sub_3=int(input("Enter the sub_3 number: "))
      total=(sub_1+sub_2+sub_3)
      avrg=total/3
      print("The total number of the three number is : ",total)
      print("The avrg number of the three number is: ", avrg) 
      
      

     
      
      
         
         
         
         
         

         
         
          
          