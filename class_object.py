


a=2
print(type(a))


''' class has two part .... 1= data/properities and 2= function/ behaivor'''
# class name should be in pascal case or camel case or snake case
# for example : PascalCase
# for example : snakeCase
# for example : Pascal_Case
# we will use snake case
# when we will create class name should be in pascal case and variabke and function will be in snake case
# https://www.visual-paradigm.com/guide/uml-unified-modeling-language/uml-class-diagram-tutorial/

''' Function vs method :

    Function 
 1. Function is block of code that is also called by its name. (independent)
 2.The function can have different parameters or may not have any at all. If any data (parameters) are passed, they are passed explicitly.
 3.It may or may not return any data.
 4.Function does not deal with Class and its instance concept.

    Method                                    
 1. Method is called by its name, but it is associated to an object (dependent).
 2. A method definition always includes ‘self’ as its first parameter.
 3.A method is implicitly passed the object on which it is invoked.
 4.It may or may not return any data.
 5. A method can operate on the data (instance variables) that is contained by the corresponding class

 '''



class Car:
    def __init__(self,windows,tyers,doors):
        self.windows=windows
        self.tyers=tyers
        self.doors=doors


car1=Car(4,4,5 )   
print(car1.doors)   
    

   