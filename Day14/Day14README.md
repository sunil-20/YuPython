# Day 14 notes
## Notes on dictionary
You can access values from a dictionary in Python using the keys associated with those values. There are a few ways to do this:

1. Using Square Brackets `[]`:

   You can access a value in a dictionary by providing the key inside square brackets.

   ```python
   my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

   # Access values by key
   name = my_dict['name']
   age = my_dict['age']

   print(f"Name: {name}, Age: {age}")
   ```

2. Using the `get()` method:

   The `get()` method allows you to access a value by specifying the key. It also provides a default value if the key doesn't exist, which can help avoid errors.

   ```python
   my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

   # Access values by key using get()
   name = my_dict.get('name')
   age = my_dict.get('age')

   print(f"Name: {name}, Age: {age}")
   ```

3. Using a for loop to iterate through the dictionary:

   You can iterate through the dictionary using a `for` loop to access both keys and values.

   ```python
   my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}

   # Access values using a for loop
   for key, value in my_dict.items():
       print(f"{key}: {value}")
   ```

Each of these methods allows you to access the values stored in a dictionary using the corresponding keys.