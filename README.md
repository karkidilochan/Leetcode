# LeetCode Solutions - NeetCode 150 Structured

This repository contains my solutions to **LeetCode problems**, structured according to the **NeetCode 150** roadmap. Each problem is categorized by topic, with a link to the problem and any relevant notes.

## 🛠 **Topics Covered**
- Arrays and Hashing
- Two Pointers
- Stack
- Binary Search
- Sliding Window
- Linked List
- Trees
- Heaps / Priority Queue
- Graphs
- Backtracking

---

Here’s your updated list with corresponding emojis for each topic:

## **📌 Problem List**  
Below is a structured table with problem links and notes. I will update this repository as I progress through the problems.  

### **🗂️ Arrays and Hashing**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Encode Decode](https://leetcode.com/problems/encode-and-decode-strings/description/) | encode: append a separator with string size, decode: loop until separator, get the size and get the string |
| 2 | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/description/) | find the start of a sequence i.e. num-1 does not exist in hashmap, then loop until its consecutive is not in hashmap | 
| 3 | [Insert Interval](https://leetcode.com/problems/insert-interval/) | linear search: find insertion point, fix ranges with min(start) and max(end), binary search: find insertion point, append to result array while fixing the range with max(end) |
| 4 | [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/) | optimized approach: two passes, first pass find prefix product shifted to right by one, suffix product shifted to right by one | 

### **🎯 Two Pointers**  
| # | Problem | Notes |
|---|---------|-------|


### **📚 Stack**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Search in Rotated Array](https://leetcode.com/problems/search-in-rotated-sorted-array/submissions/1562036908/) | Find the sorted half (if mid > end, left half is sorted), then look if target is in the sorted half, and adjust midpoint accordingly |
| 2 | [Time Based Key-Value Store](https://leetcode.com/problems/time-based-key-value-store/description/) | Store every timestamp<=given timestamp, move the right window shorter if the midpoint timestamp > given timestamp |

### **🔍 Binary Search**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [First Bad Version](https://leetcode.com/problems/first-bad-version) | check left for isbadversion, return left after binary search ends |

### **🚀 Sliding Window**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Sliding window: left pointer moves right when difference of max_freq so far and current window length exceeds allowed replacements |
| 2 | [String permutation](https://leetcode.com/problems/surrounded-regions/description/) | keep a running counter for longer array, if len exceeds required length of smaller array, decrease/remove the leftmost element |


### **🔗 Linked List**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Copy Linked List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | copy linked list with recursion, create new node before recursive call, use recursive call to assign the copy, and assign random pointer after the recursive call, use hashmap as index old -> new |
| 2 | [Add Two Numbers](https://leetcode.com/problems/add-two-numbers/) | iterate through the lists until both of them are none and carry over is 0, add modulus 10 of sum to the new node |
| 3 | [Find Duplicate](https://leetcode.com/problems/find-the-duplicate-number/) | treat list as linked list, duplicate number will create a cycle, detect cycle, then find the cycle starting point by resetting on pointer to head, you can use bit set |
|4 | [Middle of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/) | slow and fast pointer|

### **🌳 Trees**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | bfs, for each node, add its children and current level + 1 to the queue,
 and use hashmap to keep track of node values at each level |
| 2 | [Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | DFS: if dfs right child first starting with level 0, at each level append to result the first node visited -> len(result) == depth, BFS: loop through the queue at each level, the last element is the rightmost |
| 3 | [Good Nodes](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/) | keep track of max in dfs and count when max is updated, start with the root value |
| 4 | [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) | validate each node, and the subtree as well, so set a range for each dfs call, right -> node.val is min, left -> node.val is max |
| 5 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | inorder traversal of bst gives sorted elements, can keep a decreasing counter after left dfs for more efficient solution |

### **⚡ Heaps / Priority Queue**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Example Problem](https://leetcode.com/problems/example) | Example note |

### **🗺️ Graphs**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Island Perimeter](https://leetcode.com/problems/island-perimeter/) | For each element, look in all four directions, and increase perimeter count if reached at the grid edge, or grid block with "0", keep track of visited blocks and avoid them |
| 2 | [Number of Islands](https://leetcode.com/problems/number-of-islands/) | For each element, look in all four directions, and do bfs/dfs if element is "1" and has not been visited.|
| 3 | [Clone Graph](https://leetcode.com/problems/clone-graph/) | bfs/dfs to each node, keep track of new clones with hashmap, and append clones of neighbors to the clone of current node |
| 4 | [Islands & Treasure](https://leetcode.com/problems/walls-and-gates/description/) | use bfs, add neighboring lands to queue, loop through the queue at each level and accumulate steps when moving to next level, return the steps count when 0(treasure) is found. |
| 5| [Rotting Oranges](https://leetcode.com/problems/rotting-oranges/) | go through the grid to find all rotten, then run bfs to find fresh ones, update count of fresh ones at the end of run |
| 6| [Pacific and Atlantic Ocean](https://leetcode.com/problems/pacific-atlantic-water-flow/) | start from the edges of grid, keep separate sets of visited nodes in pacific and atlantic |
| 7| [Flood Fill](https://leetcode.com/problems/flood-fill/description/) | bfs/dfs the graph, check for original color after popping queue, since node in queue may be already changed |
| 8 | [01-Matrix](https://leetcode.com/problems/01-matrix/) | bfs: start from 0-cell append them to queue, after traversing the matrix, start processing the queue, traverse new cells if their results cell hasn't been computed yet, DP approach: do a two pass from top-left, and then bottom-right |
| 9 | [Surrounded Regions](https://leetcode.com/problems/surrounded-regions/description/) | we are excluding edges from modification, so start search from edges, and populate with something else then another loop to capture the rest, turn populated ones to the original value |

### **🌀 Backtracking**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Example Problem](https://leetcode.com/problems/example) | Example note |

### ** Bit Manipulation**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Single Number](https://leetcode.com/problems/single-number/description/) | Use XOR, its associative and commutative, a^a = 0, a^0 =a |

### **Dynamic Programming**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Fibonacci Sequence](https://leetcode.com/problems/fibonacci-number/description/) | Memoization(top-down): store value of n in precomputed dict, Tabulation(bottom-up): compute from 2 to n |
| 2 | [Climbing Stairs](https://leetcode.com/problems/climbing-stairs) | Think of each step of stairs as a node in a tree, taking 1 or 2 step as branches of that node, use DFS to traverse tree, return 0 if current path exceeds target value. |
| 3 | [Min Cost Climbing Stairs](https://leetcode.com/problems/min-cost-climbing-stairs/) | recursion: if current step exceeds length, return 0, memoize it for dp, for bottom up, create an array that stores min of the result of i-1 and i-2, added the cost for those previous steps  |
| 4 | [House Robber](https://leetcode.com/problems/house-robber) | subproblem: find max of each subarray for an element of the array, keep prev_1 or keep prev_2 and add self to avoid adjacent values |
| 5 | [House Robber 2](https://leetcode.com/problems/house-robber-ii/description/) | run dp for two instances: 1. if first element taken, slice out last element, 2. if second element taken iterate until last element |

