#!/usr/bin/node
function factorial (num) {
  if (isNaN(num)) return 1;
  num = parseInt(num);
  if (num === 0 || num === 1) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(process.argv[2]));