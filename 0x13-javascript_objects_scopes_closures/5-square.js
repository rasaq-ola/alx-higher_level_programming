#!/usr/bin/node
/* Write a class Square that defines a square and inherits from Rectangle of 4-rectangle.js:

You must use the class notation for defining your class and extends
The constructor must take 1 argument: size
The constructor of Rectangle must be called (by using super())
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

  rotate () {
    if (Object.keys(this).length !== 0) {
      [this.width, this.height] = [this.height, this.width]; // Swap width and height
    }
  }

  double () {
    if (Object.keys(this).length !== 0) {
      this.width *= 2;
      this.height *= 2;
    }
  }
}

class Square extends Rectangle {
  constructor (size) {
    super(size, size); // Call the constructor of Rectangle with 'size' for both width and height
  }
}
module.exports = Rectangle;
