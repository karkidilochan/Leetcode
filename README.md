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
| 2 | [Longest Consecutive Sequence] (https://leetcode.com/problems/longest-consecutive-sequence/description/) | find the start of a sequence i.e. num-1 does not exist in hashmap, then loop until its consecutive is not in hashmap | 

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
| 1 | [Example Problem](https://leetcode.com/problems/example) | Example note |

### **🚀 Sliding Window**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Longest Repeating Character Replacement](https://leetcode.com/problems/longest-repeating-character-replacement/) | Sliding window: left pointer moves right when difference of max_freq so far and current window length exceeds allowed replacements |

### **🔗 Linked List**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Copy Linked List with Random Pointer](https://leetcode.com/problems/copy-list-with-random-pointer/) | copy linked list with recursion, create new node before recursive call, use recursive call to assign the copy, and assign random pointer after the recursive call, use hashmap as index old -> new |
| 2 | [Add Two Numbers] (https://leetcode.com/problems/add-two-numbers/) | iterate through the lists until both of them are none and carry over is 0, add modulus 10 of sum to the new node |
| 3| [Find Duplicate] (https://leetcode.com/problems/find-the-duplicate-number/) | treat list as linked list, duplicate number will create a cycle, detect cycle, then find the cycle starting point by resetting on pointer to head, you can use bit set |

### **🌳 Trees**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | bfs, for each node, add its children and current level + 1 to the queue,
 and use hashmap to keep track of node values at each level |

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

### **🌀 Backtracking**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Example Problem](https://leetcode.com/problems/example) | Example note |
