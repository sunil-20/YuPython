# Blackjack capstone
To sum the values of a list in Python, you can use a loop to iterate through the list and add up its elements, or you can use the built-in `sum()` function. Here are both methods:

Method 1: Using a Loop

```python
my_list = [1, 2, 3, 4, 5]
total = 0

for num in my_list:
    total += num

print("The sum of the list is:", total)
```

Method 2: Using the `sum()` Function

```python
my_list = [1, 2, 3, 4, 5]
total = sum(my_list)

print("The sum of the list is:", total)
```

Both of these methods will calculate the sum of the values in the list `my_list` and print the result. You can replace `my_list` with your own list of values.
# List methods

In Python, lists are a commonly used data structure, and they come with a variety of built-in methods for performing operations on them. Here are some of the main list methods in Python:

1. `append(x)`: Adds an element `x` to the end of the list.

2. `extend(iterable)`: Extends the list by appending elements from the iterable (e.g., another list).

3. `insert(i, x)`: Inserts element `x` at the specified index `i`.

4. `remove(x)`: Removes the first occurrence of element `x` from the list.

5. `pop([i])`: Removes and returns the element at index `i`. If `i` is not specified, it removes and returns the last element.

6. `index(x[, start[, end]])`: Returns the index of the first occurrence of element `x` (optionally within a specified range).

7. `count(x)`: Returns the number of occurrences of element `x` in the list.

8. `sort(key=None, reverse=False)`: Sorts the list in ascending order (or descending if `reverse=True` is specified). You can provide a custom sorting key function using the `key` parameter.

9. `reverse()`: Reverses the elements of the list in place.

10. `copy()`: Returns a shallow copy of the list.

11. `clear()`: Removes all elements from the list.

12. `len(list)`: Returns the number of elements in the list.

These are some of the fundamental list methods in Python. You can use these methods to manipulate and work with lists effectively in your Python programs.
In Python, lists are a commonly used data structure, and they come with a variety of built-in methods for performing operations on them. Here are some of the main list methods in Python:

1. `append(x)`: Adds an element `x` to the end of the list.

2. `extend(iterable)`: Extends the list by appending elements from the iterable (e.g., another list).

3. `insert(i, x)`: Inserts element `x` at the specified index `i`.

4. `remove(x)`: Removes the first occurrence of element `x` from the list.

5. `pop([i])`: Removes and returns the element at index `i`. If `i` is not specified, it removes and returns the last element.

6. `index(x[, start[, end]])`: Returns the index of the first occurrence of element `x` (optionally within a specified range).

7. `count(x)`: Returns the number of occurrences of element `x` in the list.

8. `sort(key=None, reverse=False)`: Sorts the list in ascending order (or descending if `reverse=True` is specified). You can provide a custom sorting key function using the `key` parameter.

9. `reverse()`: Reverses the elements of the list in place.

10. `copy()`: Returns a shallow copy of the list.

11. `clear()`: Removes all elements from the list.

12. `len(list)`: Returns the number of elements in the list.
