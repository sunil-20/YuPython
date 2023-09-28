# Day 17 notes 
PascalCase, camelCase, snake_case
#### Simplifying the return statement without if else.
or
``` python
if a > b:
 return True
else:
 return False
```
You can simplify this code by directly returning the result of the 
comparison `a > b`, which will already yield a boolean value 
(True or False). Here's the simplified code:

```python
return a > b
```
This code will return `True` if `a` is greater than `b` and `False` otherwise, 
without the need for an explicit if-else statement.