#!/usr/bin/node
/* Write a function that returns the number of occurrences in a list:

Prototype: exports.nbOccurences = function (list, searchElement)
*/
exports.nbOccurences = function (list, searchElement) {
  // Initialize a variable to count occurrences
  let count = 0;

  // Loop through the list
  for (let i = 0; i < list.length; i++) {
    // Check if the current element matches the searchElement
    if (list[i] === searchElement) {
      count++; // Increment count if match found
    }
  }

  // Return the count of occurrences
  return count;
};
