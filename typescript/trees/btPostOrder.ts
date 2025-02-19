type BinaryNode<T> = {
  value: number;
  right: BinaryNode<T>;
  left: BinaryNode<T>;
};

function walk(curr: BinaryNode<number> | null, path: number[]): number[] {
  // base case
  if (!curr) {
    return path;
  }
  // sub steps of recursion
  // pre
  // recurse
  walk(curr.left, path);
  walk(curr.right, path);

  // post
  path.push(curr.value);

  return path;
}

export default function inOrderSearch(head: BinaryNode<number>): number[] {
  return walk(head, []);
}
