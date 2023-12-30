export default function sum(item: number): number {
  if (item === 1) {
    return 1;
  }
  return item + sum(item - 1);
}

console.log(sum(5));
