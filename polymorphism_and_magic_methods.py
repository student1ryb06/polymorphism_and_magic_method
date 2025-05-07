
class Animal:
    def sound(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name

    def __str__(self):
        return f"This is a {self.shape_name}."

dog = Dog()
cat = Cat()
circle = Shape("circle")

print(dog.sound()) 
print(cat.sound())  
print(circle)       
