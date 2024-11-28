"""
Control Flow
This topic covers:

    Conditional Statements:
        if, elif, else.
    Loops:
        for and while.
    Loop Control Statements:
        break, continue, pass.
    Comprehensions:
        List comprehensions.

Set and dictionary comprehensions.
Best Practices and Advanced Patterns.

"""
from typing import Generator

# 1. Conditional Statements
#  control the flow of execution based on conditions.
"""
if condition:
    # Code block executed if condition is True
elif another_condition:
    # Code block executed if the first condition is False and this condition is True
else:
    # Code block executed if all conditions are False

"""


def check_number(num: int) -> str:
    """
    Checks if a number is positive, negative or zero and returns a string
    indicating the same.

    Args:
        num: The number to check.

    Returns:
        A string indicating if the number is positive, negative or zero.
    """
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print(check_number(5))
print(check_number(0))
print(check_number(-3))

"""
Truthy and Falsy Values:

    Non-zero numbers, non-empty sequences, and True evaluate as truthy.
    0, None, empty sequences ([], {}, "") evaluate as falsy.
    if []:  # Evaluates to False
        print("This won't execute")

Ternary Operator:

A concise way to write simple if-else logic.
syntax: expression_if_true if condition else expression_if_false

    result = "Even" if num % 2 == 0 else "Odd"

"""

# 2. Loops
#  Used to allow repetitive execution of code.
# Iterates over a sequence (list, tuple, range, etc.).
"""
Syntax:
for item in iterable:
    # Code block executed for each item in the iterable
"""

for i in range(5):
    print(i)

"""
While Loop
Repeats as long as the condition is true.

while condition:
    # Code block executed as long as the condition is True
"""

count = 0
while count < 5:
    print(count)
    count += 1

# Iterating over collections
# 1. Lists
# 2. Tuples
# 3. Dictionaries
# 4. Sets
# 5. Strings
# 6. Ranges
# 7. Bytes
# 8. Bytearray
# 9. Memoryview

items : list[int] = [1, 2, 3, 4, 5]
for item in items:
    print(item)

tuples : tuple[int, ...] = (1, 2, 3, 4, 5)
for item in tuples:
    print(item)

dictionaries : dict[str, int] = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
for key, value in dictionaries.items():
    print(key, value)

sets : set[int] = {1, 2, 3, 4, 5}
for item in sets:
    print(item)

strings : str = "Hello, World!"
for char in strings:
    print(char)

ranges : range = range(1, 6)
for item in ranges:
    print(item)

bytes_data : bytes = b"Hello, World!"
for byte in bytes_data:
    print(byte)

bytearray_data : bytearray = bytearray(b"Hello, World!")
for byte in bytearray_data:
    print(byte)

memoryview_data : memoryview = memoryview(b"Hello, World!")
for byte in memoryview_data:
    print(byte)

# 3. Loop Control Statements
#  break, continue, pass

# break terminates the loop entirely.
for i in range(10):
    if i == 5:
        break
    print(i)

# continue skips the current iteration of the loop.
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)

# pass is a placeholder that does nothing.
# It can be used as a placeholder for empty statements or blocks of code.
for i in range(10):
    pass

# 4. Comprehensions
#  List comprehensions.
#  Dictionary comprehensions.
#  Set comprehensions.
#  Generator comprehensions.
"""
Comprehensions provide a concise way to create collections.

List Comprehensions
Syntax:
[expression for item in iterable if condition]


Dictionary Comprehensions
Syntax:
{key_expression: value_expression for item in iterable if condition}

Set Comprehensions
Syntax:
{expression for item in iterable if condition}

Generator Comprehensions
Syntax:
(expression for item in iterable if condition)

Nested Comprehensions
Syntax:
[expression for item1 in iterable1 if condition1 for item2 in iterable2 if condition2]
"""

squares: list[int] = [x * x for x in range(1, 6)]
print(squares)

even_squares: list[int] = [x * x for x in range(1, 6) if x % 2 == 0]
print(even_squares)

even_squares_dict: dict[int, int] = {x: x * x for x in range(1, 6) if x % 2 == 0}
print(even_squares_dict)

even_squares_set: set[int] = {x * x for x in range(1, 6) if x % 2 == 0}
print(even_squares_set)

even_squares_generator: Generator[int, None, None] = (x * x for x in range(1, 6) if x % 2 == 0)
print(even_squares_generator)
for x in even_squares_generator:
    print(x)

nested_comprehensions: list[int] = [x * x for x in range(1, 6) for y in range(1, 6) if x % 2 == 0 and y % 2 == 0]
print(nested_comprehensions)

"""
5. Best Practices and Advanced Patterns
Avoid Infinite Loops:

Ensure while conditions eventually evaluate to False.
Readable Comprehensions:

Avoid overly complex comprehensions. Prefer loops for clarity.
Avoid Nested Loops When Possible:

Use comprehensions, generators, or helper functions for efficiency.

Use enumerate for Indexes:
    When looping with indexes:
        for idx, value in enumerate(['a', 'b', 'c']):
            print(idx, value)
    
    
Guard Clauses in Conditionals:
Avoid nested conditionals by using guard clauses:
def process(x):
    if x < 0:
        return "Negative"
    if x == 0:
        return "Zero"
    return "Positive"

"""


