def c_to_f(C):
    return ((9/5)*C) + 32

def f_to_c(F):
    return (5/9)*(F-32)

temp = float(input("Enter a temperature "))
choice = input("Was that input Fahrenheit or Celsius : ")
if choice=="c":
    print(temp,"Celsius is",c_to_f(temp),"Fahrenheit")
else:

    print(temp, "Fahrenheit equals", f_to_c(temp), "Celsius")

