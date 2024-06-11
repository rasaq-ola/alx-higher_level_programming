#!/usr/bin/env node
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) {
  console.log(0);
} else {
  args.sort((a, b) => a - b);
  console.log(args[args.length - 2]);
}
