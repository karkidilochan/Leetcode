type BinaryNode<T> = {
  value: number;
  right: BinaryNode<T>;
  left: BinaryNode<T>;
};

export default function compare(
  a: BinaryNode<number> | null,
  b: BinaryNode<number> | null
): boolean {
  // base case(try to solve simpler cases in base case to make recursion simpler)
  if (a === null && b === null) {
    return true;
  }
  //   structural check
  if (a === null || b === null) {
    return false;
  }
  //   value check
  if (a.value !== b.value) {
    return false;
  }

  return compare(a.left, b.left) && compare(a.right, b.right);
}
