#!/usr/bin/node
exports.callMeMoby = function (x, thefunction) {
	for (let k = 0; k < x; k++) thefunction();
};
