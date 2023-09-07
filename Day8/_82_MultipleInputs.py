# Functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is the weather in {location}")
greet_with("Taylor", "London") # positional argument
greet_with(location = "London", name = "Ben") # Keyword argument