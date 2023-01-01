#Write a Python program that accepts an employee's ID, total worked hours of a month and the amount S/he received per hour. Print the employee's ID and salary (with two decimal places) of a particular month.
#  S/he has day off on Friday and Saturday. #
id=int(input("Enter the id of the employee: "))
workhour=(input("Enter the total amount of a work hour in a day: "))
h=int(workhour)
total_workhour=h*(5*3)
print("So the total workhour of a month: ",total_workhour)
work_money=(input("Enter the amount of money for an hour: "))
m=float(work_money)
total_work_money=m*total_workhour
print("All the amout of money employee received for a month is %.2f   " % total_work_money)


    
 



