#### Turtle Notes
* https://docs.python.org/3/library/turtle.html <br>
When working with Python and importing modules, there are various techniques and terms to be aware of. Here are some major notes on importing modules in Python, including the use of `from`, aliasing, and other related concepts:

1. Importing Modules:
   - Modules in Python are files containing Python code. They can include functions, classes, and variables.
   - You can import a module using the `import` statement.

   ```python
   import module_name
   ```

2. Importing Specific Items from a Module:
   - You can import specific functions, classes, or variables from a module using the `from` keyword.

   ```python
   from module_name import item_name
   ```

   For example, to import the `sqrt` function from the `math` module:

   ```python
   from math import sqrt
   ```

3. Importing Multiple Items from a Module:
   - You can import multiple items from a module by separating them with commas.

   ```python
   from module_name import item1, item2, item3
   ```

4. Aliasing:
   - You can give a module or imported item an alias using the `as` keyword. This can be helpful to provide a shorter or more descriptive name.

   ```python
   import module_name as alias_name
   from module_name import item_name as alias_name
   ```

   For example, importing the `numpy` library with an alias:

   ```python
   import numpy as np
   ```

5. Importing All Items from a Module:
   - You can import all items from a module using the `*` wildcard, but it's generally not recommended because it can lead to naming conflicts.

   ```python
   from module_name import *
   ```

6. Relative Imports:
   - In a package (a directory containing Python modules), you can use relative imports to import modules within the same package.

   ```python
   from . import module_name
   ```

7. Circular Imports:
   - Be cautious of circular imports, where two or more modules import each other directly or indirectly. This can lead to unexpected behavior or errors.

8. Built-in Modules:
   - Python has a rich standard library with built-in modules that provide various functionalities. You can import these modules without installing any external packages.

9. Virtual Environments:
   - It's a good practice to create and use virtual environments for your Python projects. This allows you to manage dependencies and isolate project-specific libraries.

10. Importing Custom Modules:
    - To import your own Python modules, ensure they are in the same directory as your script or in a directory that's on the Python path. You can then import them using their file name without the `.py` extension.

   ```python
   import my_module
   ```

These notes cover the basics of importing modules in Python, including techniques like using `from`, aliasing, and dealing with circular imports. Understanding how to organize and import modules is essential for building modular and maintainable Python code.