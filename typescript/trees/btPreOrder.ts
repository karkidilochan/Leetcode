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
  path.push(curr.value);
  // recurse
  walk(curr.left, path);
  walk(curr.right, path);
  // post
  return path;
}

export default function preOrderSearch(head: BinaryNode<number>): number[] {
  return walk(head, []);
}
