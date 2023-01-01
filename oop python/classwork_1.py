marks = float(input("Enter our marks : "))

if marks >= 80 and marks <=100:   
    print("Grade: A+")
elif marks >= 75 and marks < 80:
    print("Grade: A")
elif marks >= 70 and marks < 75:
    print("Grade: A-")
elif marks >= 60 and marks < 70:
    print("Grade: B+")
elif marks >= 50 and marks < 60:
    print("Grade: B")
elif marks >= 40 and marks < 50:
    print("Grade: C")
else:
    print("Grade: F")