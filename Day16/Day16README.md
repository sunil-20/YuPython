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

#### Python Modules
* pypi: https://pypi.org/project/prettytable/
* 
#### Instance Variable and Class Variable in OOP
In Python, instance variables and class variables are two different types of variables used in object-oriented programming. They serve distinct purposes and have different scopes and lifetimes:

1. Instance Variables:
   - Instance variables are variables that belong to a specific instance of a class.
   - They are defined within the methods of a class and are prefixed with the `self` keyword, which refers to the instance itself.
   - Each instance of a class can have its own set of instance variables, which are unique to that instance.
   - Instance variables hold data that is specific to an object's state.

   Example:
   ```python
   class Person:
       def __init__(self, name, age):
           self.name = name  # instance variable
           self.age = age    # instance variable

   person1 = Person("Alice", 30)
   person2 = Person("Bob", 25)
   ```

   In this example, `name` and `age` are instance variables, and each `person1` and `person2` object has its own set of these variables.

2. Class Variables:
   - Class variables are variables that are shared among all instances of a class.
   - They are defined within the class but outside any method, typically at the class level.
   - Class variables are not associated with any particular instance; instead, they are associated with the class itself.
   - Class variables are used to store data that is common to all objects of the class.

   Example:
   ```python
   class Circle:
       pi = 3.14159  # class variable

       def __init__(self, radius):
           self.radius = radius  # instance variable

       def calculate_area(self):
           return Circle.pi * self.radius ** 2
   ```

   In this example, `pi` is a class variable, and all instances of the `Circle` class share the same value of `pi`.

In summary, the main differences between instance variables and class variables in Python are their scope and purpose. Instance variables are specific to each instance of a class and hold data related to that instance's state, while class variables are shared among all instances of a class and are used for storing data that is common to the class itself.

#### Why use of Self keyword is helpful
In Python, when you define instance variables within a class, it's a common practice to initialize them within the class's constructor method (usually named `__init__`) and associate them with the `self` keyword. This practice has several reasons and benefits:

1. **Instance Ownership:** By initializing variables with `self`, you explicitly associate them with the instance of the class. This means that each instance of the class will have its own set of these variables, and they won't interfere with variables of the same name in other instances. This is crucial for encapsulation and maintaining the state of individual objects.

2. **Access to Attributes:** Initializing instance variables with `self` allows you to access and modify those attributes throughout the class's methods. Without `self`, you wouldn't be able to access these variables outside of the `__init__` method.

3. **Clarity and Convention:** Using `self` is a widely accepted convention in Python. When someone reads your code, it's immediately clear that you are dealing with instance variables. It also helps distinguish instance variables from local variables within methods.

4. **Default Values:** You can provide default values for instance variables during initialization. This ensures that even if a value is not explicitly provided when creating an instance, the variable will have a meaningful default value.

Here's an example to illustrate these points:

```python
class Person:
    def __init__(self, name, age=0):
        # Initializing instance variables with self
        self.name = name
        self.age = age

    def celebrate_birthday(self):
        # Accessing instance variables within a method
        self.age += 1

# Creating instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob")

# Accessing and modifying instance variables
print(person1.name)  # "Alice"
print(person1.age)   # 30

person2.celebrate_birthday()
print(person2.age)   # 1 (default age value incremented)
```

In this example, `self.name` and `self.age` are instance variables initialized within the `__init__` method. They belong to each instance of the `Person` class and can be accessed and modified using the `self` keyword.