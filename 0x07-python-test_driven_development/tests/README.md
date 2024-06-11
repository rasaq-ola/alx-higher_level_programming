# Python Test Driven Development

This project contains several Python functions and their corresponding test cases.

## Functions

1. **add_integer(a, b=98)**:
   - Adds two integers.
   - Raises TypeError if inputs are not integers or floats.

2. **matrix_divided(matrix, div)**:
   - Divides all elements of a matrix by a given divisor.
   - Raises TypeError for invalid inputs and ZeroDivisionError for division by zero.

3. **say_my_name(first_name, last_name="")**:
   - Prints "My name is <first name> <last name>".
   - Raises TypeError if inputs are not strings.

4. **print_square(size)**:
   - Prints a square with the character '#'.
   - Raises TypeError if size is not an integer and ValueError if size is negative.

5. **text_indentation(text)**:
   - Prints a text with 2 new lines after each of these characters: ., ?, :
   - Raises TypeError if text is not a string.

6. **max_integer(list=[])**:
   - Finds and returns the maximum integer in a list of integers.
   - Returns None if the list is empty.

## Tests

Each function has corresponding test cases located in the `tests/` directory. Tests can be run using the `doctest` and `unittest` modules.

### Running Tests

To run doctest cases:
```bash
python3 -m doctest ./tests/*.txt
