#!/usr/bin/node
/**
 * checks parameters
 */
class Rectangle {
	constructor (w, h) {
		if (typeof w === 'number' && w > 0 && typeof h === 'number' && h > 0) {
			this.width = w;
			this.height = h;
		}
	}

	print () {
		for (let k = 0; k < this.height; k++) {
			let myVar = '';
			let y = 0;
			while (y < this.width) {
				myVar += 'X';
				y++;
			}

			console.log(myVar);
		}
	}

	rotate () {
		let t = 0;
		t = this.width;
		this.width = this.height;
		this.height = t;
	}

	double () {
		this.width *= 2;
		this.height *= 2;
	}
}
module.exports = Rectangle;
