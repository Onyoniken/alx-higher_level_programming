#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
	let c = 0;

	for (let k = 0; k < list.length; k++) {
		c = (list[k] === searchElement ? c + 1 : c);
	}

	return c;
};
