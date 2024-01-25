type SNode<T> = {
  value: T;
  prev: SNode<T>;
};

export default class Stack<T> {
  public length: number;
  private head?: SNode<T>;

  constructor() {
    this.head = undefined;
    this.length = 0;
  }

  push(item: T): void {
    const new_node = { value: item } as SNode<T>;

    if (!this.head) {
      this.head = new_node;
      this.length++;
      return;
    }

    new_node.prev = this.head;
    this.head = new_node;
    this.length++;
  }

  pop(): T | undefined {
    this.length = Math.max(0, this.length - 1);
    if (!this.head) {
      return undefined;
    }
    const old_head = this.head;
    this.head = this.head.prev;
    return old_head.value;
  }

  peek(): T | undefined {
    return this.head?.value;
  }
}
