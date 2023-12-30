export default function bubbleSort(haystack: number[]) {
  for (let i = 0; i < haystack.length; i++) {
    for (let j = 0; j < haystack.length - 1 - i; j++) {
      // swap the values
      if (haystack[j] > haystack[j + 1]) {
        const temp = haystack[j];
        haystack[j] = haystack[j + 1];
        haystack[j + 1] = temp;
      }
    }
  }
  return haystack;
}

// immutable arrays are poor performing data structures
// they provide ease of use, but comes at cost of space and replicating it.
