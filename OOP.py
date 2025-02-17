 class Car:
   def __init__(self, make, model, year):
    self.make = make
    self.model = model
    self.year = year
    my_car = Car("Toyota", "Corolla", 2022)
    my_car.start()
 def start(self):
   print(f"The {self.year} {self.make} {self.model} is starting.")


 class Person:
  def __init__(self, name, age):
   self.name = name # Public attribute
   self.__age = age # Private attribute
   def get_age(self):
    return self.__age   
   
 class Animal:
  def speak(self):
   print("Animal speaks")
 class Dog(Animal):
  def bark(self):
   print("Dog barks")
 dog = Dog()
 dog.speak() # Inherited method
 dog.bark() # Child class method   


 class Animal:
  def speak(self):
   print("Animal speaks")
 class Dog(Animal):
   def speak(self):
    print("Dog barks")
 class Cat(Animal):
  def speak(self):
   print("Cat meows")
 def animal_sound(animal):
  animal.speak() # Calls the correct method depending on the object type
 dog = Dog()
 cat = Cat()
 animal_sound(dog) # Output: Dog barks
 animal_sound(cat) # Output: Cat meow


 class Shape(ABC):
  @abstractmethod
  def area(self):
   pass
 class Circle(Shape):
  def __init__(self, radius):
   self.radius = radius
 def area(self):
  return 3.14 * (self.radius ** 2)
 circle = Circle(5)
 print(circle.area()) # Output: 78.5