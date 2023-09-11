# Day 12 notes Local and Global Scopes
In Python, variables can exist in different scopes, and the two most common scopes are local scope and global scope. These scopes determine where a variable can be accessed and modified within a Python program.

1. **Local Scope:**
   
   - **Definition**: A local scope refers to the innermost scope within a Python program. Variables defined within a function or a code block (such as a loop or conditional statement) are in the local scope.
   
   - **Access**: Variables in a local scope can only be accessed and modified from within the same function or code block where they are defined. They are not visible or accessible from outside that function or block.
   
   - **Lifetime**: The lifetime of a local variable is limited to the duration of the function or code block in which it is defined. It is created when the function or block is entered and destroyed when it exits.

   Example of local scope:

   ```python
   def my_function():
       x = 10  # x is in the local scope of my_function
       print(x)  # Accessing x within the same function

   my_function()
   # print(x)  # This would result in an error because x is not defined in the global scope
   ```

2. **Global Scope:**
   
   - **Definition**: The global scope is the outermost scope in a Python program. Variables defined at the top level of a Python script or module, outside of any functions or code blocks, are in the global scope.
   
   - **Access**: Variables in the global scope can be accessed and modified from anywhere in the program, both inside and outside functions or code blocks.
   
   - **Lifetime**: The lifetime of a global variable extends throughout the entire program's execution, from the point it is defined until the program terminates.

   Example of global scope:

   ```python
   y = 20  # y is in the global scope

   def my_function():
       print(y)  # Accessing y within the function

   my_function()
   print(y)  # Accessing y outside the function
   ```

It's important to understand and manage variable scope in Python, as it helps prevent naming conflicts and ensures that variables are used in the intended context. If a variable is not found in the local scope, Python will look for it in higher scopes, including the global scope, until it finds a match or reaches the global scope. If it's not found in any scope, a `NameError` will be raised.
Certainly! Let's use an everyday scenario to explain local and global scope in a more human-friendly way.

**Local Scope Example (Kitchen):**

Imagine you're in your kitchen, and you have a recipe book open on the counter. You decide to make a sandwich, so you start gathering ingredients and following the recipe. In this scenario:

- The kitchen is like a local scope. It's the place where you're working on a specific task, which is making a sandwich.

- The ingredients and utensils you use within the kitchen (local scope) are like variables in a local scope. They are specific to your task of making a sandwich and aren't visible or accessible from outside the kitchen.

- If you need a knife, you can find it in your kitchen (local scope), but you can't magically pull out ingredients from your neighbor's kitchen (global scope) unless you go to their kitchen (access the global scope).

**Global Scope Example (Neighborhood):**

Now, let's expand the scenario to your neighborhood:

- Your kitchen (local scope) is just one part of your neighborhood (global scope).

- In your neighborhood, there's a shared garden where everyone can access and pick fruits. Let's say there's an apple tree in the garden, and it has some apples.

- You can go to the garden (global scope) and pick apples from the tree. The apples in the garden are like global variables. They are accessible from different places within your neighborhood (global scope).

- However, you can't bring the whole garden into your kitchen (local scope). Instead, you pick some apples from the garden and bring them into your kitchen to use them in your sandwich-making task.

In summary, local scope is like the specific area where you're working on a task (e.g., your kitchen for making a sandwich), and global scope is like a larger area where things are accessible from various places (e.g., your neighborhood's shared garden with apples). Variables (ingredients/tools) in a local scope are specific to the task at hand, while global variables can be accessed from different parts of the program (or neighborhood).

* Name space is valid in certain scope. 
* There is no Block Scope