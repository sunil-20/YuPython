#### Day 9 notes Dictionaries & Nesting
* Dictionary consists of key, value pairs in curly braces.
Dictionaries in Python are unordered collections of key-value pairs. They are a fundamental data structure in Python and are also known as associative arrays, hash maps, or hash tables in other programming languages. Here are some key points to understand about Python dictionaries:

1. **Key-Value Pairs:** Each element in a dictionary is a key-value pair. The key is a unique identifier for a specific value in the dictionary.

2. **Unordered:** Dictionaries are unordered, which means the order of elements is not guaranteed. In Python 3.7 and later versions, dictionaries maintain the insertion order, meaning that elements are stored in the order they were added. In Python 3.6 and earlier, dictionaries are not ordered.

3. **Mutable:** Dictionaries are mutable, meaning you can add, update, or remove key-value pairs after creating a dictionary.

4. **Keys Are Unique:** Keys in a dictionary must be unique. If you attempt to add a duplicate key, the new value will overwrite the existing one.

5. **Keys Are Immutable:** Keys must be of an immutable data type (e.g., strings, numbers, or tuples). This is because dictionaries use the keys as hash values to store and retrieve values efficiently.

6. **Values Can Be Any Data Type:** Values associated with keys in a dictionary can be of any data type, including numbers, strings, lists, other dictionaries, or custom objects.

7. **Accessing Values:** You can access values in a dictionary by using square brackets `[]` and providing the key. For example, `my_dict['key']` retrieves the value associated with the key `'key'`.

8. **Common Dictionary Operations:** Some common operations on dictionaries include adding new key-value pairs, updating existing values, deleting key-value pairs, checking if a key exists, iterating through keys or values, and getting the number of key-value pairs.

Here's an example of a dictionary in Python:

```python
# Creating a dictionary
my_dict = {
    'name': 'John',
    'age': 30,
    'city': 'New York'
}

# Accessing values by key
name = my_dict['name']  # 'John'
age = my_dict['age']    # 30
city = my_dict['city']  # 'New York'

# Adding a new key-value pair
my_dict['occupation'] = 'Engineer'

# Updating a value
my_dict['age'] = 31

# Deleting a key-value pair
del my_dict['city']

# Checking if a key exists
if 'name' in my_dict:
    print(f"The 'name' key exists with the value '{my_dict['name']}'")

# Iterating through keys
for key in my_dict:
    print(key, my_dict[key])
```

Dictionaries are widely used in Python for tasks such as data storage, configuration settings, and efficient data retrieval based on keys. They provide a convenient and flexible way to organize and access data in your Python programs.