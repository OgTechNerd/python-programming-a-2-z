""" The class statement creates a class object and assigns it a name. Just like the function def statement, the Python class statement is an executable statement.
When reached and run, it generates a new class object and assigns it to the name in the class header. Also, like defs, class statements typically run when the files
they are coded in are first imported

Assignments inside class statements make class attributes. Just like in module files, top-level assignments within a class statement (not nested in a def) generate
attributes in a class object. Technically, the class statement defines a local scope that morphs into the attribute namespace of the class object, just like a module’s
global scope. After running a class statement, class attributes are accessed by name qualification: object.name

Class attributes provide object state and behavior. Attributes of a class object record state information and behavior to be shared by all instances created from
the class; function def statements nested inside a class generate methods, which process instances.

    Returns:
        _type_: _description_
"""


class Vehicle():
    def __init__(self, material=str, wheels=int, model=str, speed=int): # constructor
         self.build = material
         self.drive = wheels
         self.model = model
         self.speed = speed 
    def getSpeed(self, dist, time) -> int:
        self.dist = dist  # in Km
        self.time = time  # in hr
        return dist/time  # kmph
    def setSpeed(self, speed) -> int:
        self.speed = speed
        return speed # kmph

        """if you dont define a constructor
           then Python creates default constructor
        """

class Employee():
    def computeSalary():
        pass
    def giveRaise():
        pass
    def promote():
        pass
    def retire():
        pass

"""his time, we’ll define a subclass of the prior section’s Second Class that implements three specially  attributes that Python will call automat-ically:
• __init__ is run when a new instance object is created: self is the new object.1
• __add__ is run when a ThirdClass instance appears in a + expression.
• __str__ is run when an object is printed (technically, when it’s converted to its
print string by the str built-in function or its Python internals equivalent)
"""    
class Person():
    def __init__(self, name, age):
      self.name = name
      self.age = age
      
    def __add__(self, age):
        return (self.age += age)
    def __str__(self) -> str:
        return (f"This person's name is {self.name} and age is {self.age}")
    
newCar = Vehicle("Steel", 4, "Maruti-Swift", 30)
print(newCar.speed)
print(newCar.setSpeed(40))
    
        
        
        