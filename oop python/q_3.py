# create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
class circle():
    
    def __init__(self, radius):
        
        self.radius = radius
        
    def getArea(self):
        return 3.14*self.radius*self.radius
    def getCircumference(self):
        return 2*3.14*self.radius
c1=circle(int(input("Enter the radius of the circle: ")))
print("The area of circle is: ", c1.getArea())
print("The circumference of circle is: ", c1.getCircumference())