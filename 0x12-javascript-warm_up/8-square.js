#!/usr/bin/node
const x = process.argv[2];

if (!parseInt(x)) {
	console.log('Missing size');
} else {
	for (let k = 0; k < x; k++) {
		let l = 0;
		let myVar = '';

		while (l < x) {
			myVar = myVar + 'X';
			l++;
		}
		console.log(myVar);
	}
}

