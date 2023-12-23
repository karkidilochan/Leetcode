export default function linearSearch(
  searchSpace: number[],
  item: number
): boolean {
  for (let i = 0; i < searchSpace.length; ++i) {
    if (searchSpace[i] == item) {
      return true;
    }
  }
  return false;
}

console.log(linearSearch([1, 2, 3, 4, 5], 6));
