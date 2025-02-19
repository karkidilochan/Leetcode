"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
function binarySearch(haystack, needle) {
    var start = 0;
    var end = haystack.length;
    var midpoint, value;
    do {
        midpoint = Math.floor((start + end) / 2);
        value = haystack[midpoint];
        if (value === needle) {
            return true;
        }
        else if (value > needle) {
            end = midpoint;
        }
        else {
            start = midpoint + 1;
        }
    } while (start < end);
    return false;
}
exports.default = binarySearch;
console.log(binarySearch([1, 2, 3, 4, 5], 3));
