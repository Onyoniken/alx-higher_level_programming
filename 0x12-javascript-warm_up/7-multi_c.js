#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
	console.log('Missing number of occurrences');
} else {
  for (let k = 0; k < x; k++) {
	  console.log('C is fun');
  }
}
