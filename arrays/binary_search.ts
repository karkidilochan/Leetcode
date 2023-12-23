export default function binarySearch(
  haystack: number[],
  needle: number
): boolean {
  let start = 0;
  let end = haystack.length;
  let midpoint: number, value: number;

  do {
    midpoint = Math.floor((start + end) / 2);
    value = haystack[midpoint];

    if (value === needle) {
      return true;
    } else if (value > needle) {
      end = midpoint;
    } else {
      start = midpoint + 1;
    }
  } while (start < end);
  return false;
}

console.log(binarySearch([1, 2, 3, 4, 5], 6));
