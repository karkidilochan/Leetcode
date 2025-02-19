"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function linearSearch(searchSpace, item) {
    for (var i = 0; i < searchSpace.length; ++i) {
        if (searchSpace[i] == item) {
            return true;
        }
    }
    return false;
}
exports.default = linearSearch;
console.log(linearSearch([1, 2, 3, 4, 5], 4));
