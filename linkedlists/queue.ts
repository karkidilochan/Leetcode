type Node<T> = {
  value: T;
  next?: Node<T>;
};

export default class Queue<T> {
  public length: number;
  private head?: Node<T>;
  private tail?: Node<T>;

  constructor() {
    // initialize the parameters
    this.head = this.tail = undefined;
    this.length = 0;
  }

  //   add to tail
  enqueue(item: T): void {
    const new_node = { value: item } as Node<T>;
    this.length++;

    if (!this.tail) {
      // create a new queue
      this.tail = this.head = new_node;
      return;
    }
    this.tail.next = new_node;
    this.tail = new_node;
  }

  // remove from head
  dequeue(): T | undefined {
    if (!this.head) {
      return undefined;
    }
    this.length--;
    const old_head = this.head;
    this.head = this.head.next;
    old_head.next = undefined;
    return old_head.value;
  }

  peek(): T | undefined {
    return this.head?.value;
  }
}
