# Primitive Types
# 1. int: Represents integers (whole numbers, both positive and negative).
from typing import Union, Any, Literal

age: int = 25
large_number: int = 10**18 # 1000000000000000000 :==> can store arbitrary large numbers


# 2. float: Represents floating-point numbers (decimal values).

pi: float = 3.14159
temperature: float = 37.5 # 37.5 degrees Celsius
scientific: float = 1.2e-3 # 0.0012 in scientific notation

# 3. bool: Represents boolean values (True or False).

is_raining: bool = True
is_sunny: bool = False
is_active: bool = True
is_zero: bool = (0 == 0) # Evaluates to True

# 4. str: Represents strings (sequence of Unicode characters).

name: str = "Aakash"
greeting: str = "Hello, " + name
multiline_string: str = """
This is a
multi-line
string.
"""

# 5. complex: Represents complex numbers (real and imaginary parts).

complex_number: complex = 3 + 2j
another_complex_number: complex = complex(3, 2)
added_complex_number: complex = complex_number + another_complex_number
multiplied_complex_number: complex = complex_number * another_complex_number
print(added_complex_number) # output: (6+4j)
print(multiplied_complex_number) # output: (5+12j)

# 6. None: Represents the absence of a value.

response: None = None
def do_nothing() -> None:
    """Does nothing.

    This function takes no arguments and simply passes without doing anything.
    """
    pass

# 7. bytes: Represents bytes (sequence of bytes).

bytes_data: bytes = b"Hello, world!"
print(bytes_data) # output: b'Hello, world!'

# 8. bytearray: Represents mutable bytes (sequence of bytes).

bytearray_data: bytearray = bytearray(b"Hello, world!")
print(bytearray_data) # output: bytearray(b'Hello, world!')

# 9. memoryview: Represents a view of a memory region (sequence of bytes).

memoryview_data: memoryview = memoryview(b"Hello, world!")
print(memoryview_data) # output: <memory at 0x104fa3b80>

# Collection Types
# 1. list: Represents an ordered sequence of elements.
# Mutable, Ordered collection

my_list: list[int] = [1, 2, 3]
my_list.append(4)
print(my_list) # output: [1, 2, 3, 4]

# 2. tuple: Represents an ordered sequence of elements.
# Immutable, Ordered collection

my_tuple: tuple[int, int, int] = (1, 2, 3)
print(my_tuple) # output: (1, 2, 3)

# 3. set: Represents an unordered collection of unique elements.
# Mutable, Unordered collection, Unique elements

my_set: set[int] = {1, 2, 3}
my_set.add(3)
print(my_set) # output: {1, 2, 3}

# 4. dict: Represents a mapping of keys to values.
# Mutable, Unordered collection, Unique keys

my_dict: dict[str, int] = {"a": 1, "b": 2, "c": 3}
my_dict["d"] = 4
print(my_dict) # output: {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# 5. frozenset: Represents an immutable set.
# Immutable, Unordered collection, Unique elements

my_frozenset: frozenset[int] = frozenset({1, 2, 3})
print(my_frozenset) # output: frozenset({1, 2, 3})

# 6. range: Represents a sequence of integers.
# Immutable, Ordered collection

my_range: range = range(5)
print(list(my_range)) # output: [0, 1, 2, 3, 4]

"""
Lists vs Tuples:
    Lists are faster for element access, slower for iteration.
    Tuples are often used when the collection shouldn’t change.
    
Dictionaries:
    Keys must be hashable (immutable types like str, int, or tuples of immutables).
    Iterating over keys, values, or items is order-preserving since Python 3.7.
    
Sets and Frozensets:
    Sets are efficient for membership checks (O(1) for in).
    Frozensets are hashable, so they can be used as keys in dictionaries or elements in sets.

"""

# Special Types (via Typing Modules)
# 1. Union: Combines multiple types into a single type.

def add(a: int | float, b: Union[int, float]) -> int | float:
    """
    Adds two numbers together.

    Args:
        a: The first number.
        b: The second number.

    Returns:
        The sum of the two numbers.
    """
    return a + b

print(add(1, 2))        # Output: 3
print(add(1.0, 2.0))    # Output: 3.0

# 2. Any: Represents any type.(skips type checking)

def print_any(a: Any) -> None:
    """
    Prints any object.

    Args:
        a: The object to print.
    """
    print(f"Data: {a}")

print_any(1)                # Output: Data: 1
print_any("Hello, world!")  # Output: Data: Hello, world!
print_any([1, 2, 3])        # Output: Data: [1, 2, 3]

# 3. Optional: Represents an optional value. Represents a type or None (shortcut for Union[type, None]).

def get_user_name(user_id: int) -> str | None:
    """
    Returns the name of a user.

    Args:
        user_id: The ID of the user.

    Returns:
        The name of the user, or None if the user is not found.
    """
    if user_id > 0:
        return "John Doe"
    return None

get_user_name(1)    # Output: John Doe
get_user_name(-1)   # Output: None

# 4. Literal: Represents a literal value.Defines exact values allowed for a type.
def set_status(status: Literal["active", "inactive"]) -> str:
    """
    Sets the status to the given value.

    Args:
        status: The status to set, either "active" or "inactive".

    Returns:
        A string indicating the status that was set.
    """
    return f"Status set to {status}"

print(set_status("active"))     # Output: Status set to active
print(set_status("inactive"))   # Output: Status set to inactive

# 5. NewType: Creates a new type alias.

from typing import NewType

UserId = NewType("UserId", int)

def get_user_name(user_id: UserId) -> str:
    """
    Returns the name of a user.

    Args:
        user_id: The ID of the user.

    Returns:
        The name of the user.
    """
    return f"User with {user_id}"

print(get_user_name(UserId(1)))     # Output: User with 1
print(get_user_name(UserId(-1)))    # Output: User with -1

# 6. TypedDict: Creates a new type alias.

from typing import TypedDict

User = TypedDict("User", {
    "name": str,
    "age": int,
    "email": str
})

def get_user_name(user: User) -> str:
    """
    Returns the name of a user.

    Args:
        user: The user object.

    Returns:
        The name of the user.
    """
    return user["name"]

print(get_user_name({"name": "John Doe", "age": 30, "email": "aakash.work.001@gmail"}))  # Output: John Doe