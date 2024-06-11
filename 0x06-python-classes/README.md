# Square Class Project

This project contains Python classes that define a square and its properties.

## Files

* `0-square.py`: Defines an empty class `Square`.
* `1-square.py`: Defines a class `Square` with a private instance attribute `size`.
* `2-square.py`: Defines a class `Square` with a private instance attribute `size`, with validation for type and value.
* `3-square.py`: Defines a class `Square` with a private instance attribute `size`, with validation for type and value, and a method to calculate the area.
* `4-square.py`: Defines a class `Square` with a private instance attribute `size`, with validation for type and value, a method to calculate the area, and getter/setter methods for `size`.
* `5-square.py`: Defines a class `Square` with a private instance attribute `size`, with validation for type and value, a method to calculate the area, getter/setter methods for `size`, and a method to print the square.
* `6-square.py`: Defines a class `Square` with private instance attributes `size` and `position`, with validation for type and value, a method to calculate the area, getter/setter methods for `size` and `position`, and a method to print the square.

## Usage

To use these classes, simply import them into your Python scripts and create instances of the `Square` class with the desired size and position parameters.

Example:

```python
from 6-square import Square

# Create a square with size 5 and position (1, 2)
my_square = Square(5, (1, 2))

# Print the area of the square
print("Area:", my_square.area())

# Print the square
my_square.my_print()
