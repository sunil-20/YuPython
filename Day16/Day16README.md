#### OOP
Object-Oriented Programming (OOP) is a programming paradigm that is widely used in Python and many other programming languages. In OOP, the fundamental concept is the "object," which is a self-contained unit that represents a real-world entity or concept. Objects are instances of classes, which are templates or blueprints that define the structure and behavior of objects. Python is an object-oriented programming language that supports OOP principles, and here are some key concepts in OOP in Python:

1. **Classes and Objects:**
   - A class is a blueprint or template for creating objects. It defines the attributes (data) and methods (functions) that the objects of the class will have.
   - An object is an instance of a class. It is a concrete realization of the class, with its own unique data and state.

   Example:
   ```python
   class Car:
       def __init__(self, make, model):
           self.make = make
           self.model = model

       def start_engine(self):
           print(f"{self.make} {self.model}'s engine started.")

   # Creating objects
   car1 = Car("Toyota", "Camry")
   car2 = Car("Ford", "Mustang")

   # Accessing object attributes and methods
   print(car1.make)  # Output: Toyota
   car2.start_engine()  # Output: Ford Mustang's engine started.
   ```

2. **Inheritance:**
   - Inheritance allows you to create a new class that inherits attributes and methods from an existing class (base or parent class).
   - The new class is called a derived or subclass, and it can add or override attributes and methods.

   Example:
   ```python
   class ElectricCar(Car):  # ElectricCar is a subclass of Car
       def __init__(self, make, model, battery_capacity):
           super().__init__(make, model)  # Call the constructor of the parent class
           self.battery_capacity = battery_capacity

       def start_engine(self):
           print(f"{self.make} {self.model}'s electric motor started.")

   e_car = ElectricCar("Tesla", "Model S", "100 kWh")
   e_car.start_engine()  # Output: Tesla Model S's electric motor started.
   ```

3. **Encapsulation:**
   - Encapsulation is the practice of bundling the data (attributes) and the methods (functions) that operate on the data within a single unit (i.e., the class).
   - It helps in hiding the internal implementation details and exposing a clean interface to the outside world.

4. **Polymorphism:**
   - Polymorphism allows objects of different classes to be treated as objects of a common superclass.
   - It enables you to write more generic code that can work with objects of different types.

   Example:
   ```python
   def start_vehicle(vehicle):
       vehicle.start_engine()

   car = Car("Toyota", "Corolla")
   e_car = ElectricCar("Nissan", "Leaf", "40 kWh")

   start_vehicle(car)     # Output: Toyota Corolla's engine started.
   start_vehicle(e_car)   # Output: Nissan Leaf's electric motor started.
   ```

5. **Abstraction:**
   - Abstraction is the process of simplifying complex systems by modeling classes based on the essential properties and behaviors relevant to the problem domain, while hiding unnecessary details.

OOP in Python is a powerful paradigm that helps in organizing code, making it more modular, reusable, and easier to maintain. It encourages the modeling of real-world concepts, making it particularly useful for projects with complex structures and relationships.

#### Additional description of a class
In layman's terms, think of a class as a blueprint or a template for creating objects. Imagine you want to build a house. Before you actually build it, you create a detailed plan or blueprint that specifies how the house should look and what its features should be. This blueprint contains information about the number of rooms, their sizes, the layout, the color of the walls, and so on.

In the world of programming, a class is like that blueprint. It defines the structure and behavior of objects that you want to create in your program. It specifies what data (attributes or properties) an object should have and what actions (methods or functions) it can perform.

Once you have this blueprint (class), you can use it to create multiple objects (instances) that share the same characteristics and behaviors, just like you can use the same house blueprint to build many houses with the same design.

So, a class is like a recipe for creating objects with predefined properties and behaviors, helping you organize and manage your code in a structured way.

#### Turtle module
* Turtle resource: https://docs.python.org/3/library/turtle.html
* Turtle color: https://cs111.wellesley.edu/reference/colors


