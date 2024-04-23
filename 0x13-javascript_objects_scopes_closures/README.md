# Higher Level Programming - JavaScript

## Description
This repository contains solutions to JavaScript programming tasks assigned in the Higher Level Programming curriculum at Holberton School.

## Files

| Filename | Description |
| -------- | ----------- |
| [0-rectangle.js](./0-rectangle.js) | Empty class `Rectangle` that defines a rectangle |
| [1-rectangle.js](./1-rectangle.js) | Class `Rectangle` that defines a rectangle, with constructor arguments `w` and `h` |
| [2-rectangle.js](./2-rectangle.js) | Class `Rectangle` that defines a rectangle, with constructor arguments `w` and `h`, and handles cases where `w` or `h` are 0 or negative |
| [3-rectangle.js](./3-rectangle.js) | Class `Rectangle` that defines a rectangle, with constructor arguments `w` and `h`, handles cases where `w` or `h` are 0 or negative, and contains a method `print()` to print the rectangle using the character 'X' |
| [4-rectangle.js](./4-rectangle.js) | Class `Rectangle` that defines a rectangle, with constructor arguments `w` and `h`, handles cases where `w` or `h` are 0 or negative, contains a method `print()` to print the rectangle using the character 'X', a method `rotate()` to exchange the width and height of the rectangle, and a method `double()` to multiply the width and height of the rectangle by 2 |
| [5-square.js](./5-square.js) | Class `Square` that defines a square, inherits from `Rectangle` of `4-rectangle.js`, and has a constructor that takes one argument `size` |
| [6-square.js](./6-square.js) | Class `Square` that defines a square, inherits from `Square` of `5-square.js`, and contains an instance method `charPrint(c)` to print the rectangle using the character `c`, or 'X' if `c` is undefined |
| [7-occurrences.js](./7-occurrences.js) | Function `nbOccurences` that returns the number of occurrences in a list |
| [8-esrever.js](./8-esrever.js) | Function `esrever` that returns the reversed version of a list |
| [9-logme.js](./9-logme.js) | Function `logMe` that prints the number of arguments already printed and the new argument value |
| [10-converter.js](./10-converter.js) | Function `converter` that converts a number from base 10 to another base passed as an argument |
- **100-map.js:** Script that imports an array and computes a new array where each value is equal to the value of the initial list multiplied by its index.

- **101-sorted.js:** Script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.

- **102-concat.js:** Script that concatenates two files.

## Files

- **100-data.js:** Contains the initial list for script `100-map.js`.
- **101-data.js:** Contains the dictionary of occurrences for script `101-sorted.js`.

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- All scripts are interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All files end with a new line
- The first line of all files is `#!/usr/bin/node`
- All files must be executable
- All files are semistandard-compliant (standard JS style with semicolons)
- No use of `var`
