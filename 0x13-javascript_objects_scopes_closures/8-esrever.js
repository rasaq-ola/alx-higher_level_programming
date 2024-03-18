#!/usr/bin/node
/* Write a function that returns the reversed version of a list:

Prototype: exports.esrever = function (list)
You are not allow to use the built-in method reverse
*/
exports.esrever = function (list) {
  let len = list.length - 1;
  let i = 0;
  while ((len - i) > 0) {
    const aux = list[len];
    list[len] = list[i];
    list[i] = aux;
    i++;
    len--;
  }
  return list;
};
