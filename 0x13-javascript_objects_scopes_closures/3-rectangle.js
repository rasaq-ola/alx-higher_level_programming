#!/usr/bin/node;
/* Write a class Rectangle that defines a rectangle:

You must use the class notation for defining your class
The constructor must take 2 arguments: w and h
Initialize the instance attribute width with the value of w
Initialize the instance attribute height with the value of h
If w or h is equal to 0 or not a positive integer, create an empty object
Create an instance method called print() that prints the rectangle using the character X
*/
class Rectangle {
  constructor (w, h) {
    if (typeof w !== 'number' || typeof h !== 'number' || w <= 0 || h <= 0) {
      return {}; // Return an empty object if width or height is invalid
    }
    this.width = w;
    this.height = h;
  }

  print () {
    if (Object.keys(this).length === 0) {
      console.log(''); // Print an empty line if the object is empty
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log('X'.repeat(this.width)); // Print 'X' repeated width times for each row
      }
    }
  }
}
module.exports = Rectangle;
