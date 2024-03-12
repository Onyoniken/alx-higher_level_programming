#!/usr/bin/node
/**
 * square inheriting from prevous class
 */
const PrevSquare = require('./5-square');

class Square extends PrevSquare {
	charPrint (c) {
		const myChar = c === undefined ? 'X' : c;
		for (let k = 0; k < this.height; k++) {
			let myVar = '';
			let y = 0;
			while (y < this.width) {
				myVar += myChar;
				y++;
			}

			console.log(myVar);
		}
	}
}
module.exports = Square;
