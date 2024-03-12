#!/usr/bin/node

exports.esrever = function (list) {
	const reversedList = [];
	for (let k = list.length - 1; k >= 0; k--) {
		reversedList.push(list[k]);

}

	return (reversedList);
};

