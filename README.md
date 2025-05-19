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
| 5 | [Ransom Note](https://leetcode.com/problems/ransom-note/) | keep count of each character and use O(1) lookup |
| 6 | [Merge Intervals](https://leetcode.com/problems/merge-intervals/) | condition to merge intervals: start<=last_end and end>=last_start,
sort the intervals to get a sequence of ascending intervals |
| 7 | [Sort Colors](https://leetcode.com/problems/sort-colors/) |naive: use hashmap, in-place solution using dutch national flag algorithm
O(n) time complexity, O(1) space complexity
use three pointers: current, zero, and two, iterate until two pointer and swap values |
| 8 | [Majority Element](https://leetcode.com/problems/majority-element/) | boyer-Moore Voting Algorithm
the majority element's count remain when subtracted by counts of all other elements |
| 9 | [Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/) | water at each point is min(leftmax, rightmax) - height
two passes to find leftmax and rightmax for each point
for 2p, use left,right pointers to find leftmax and rightmax
update the smallest of leftmax and rightmax with +1 and find unit by subtracting
height from the smallest of leftmax and rightmax |
| 10 | [Car Fleet](https://leetcode.com/problems/car-fleet/) | need to look at cars from descending order of position,
faster cars with lesser time catch up to slower cars with greater time
in descending order, if time of car greater than the car in front of it, increase fleet count
can use stack to keep track of the time of the car in front of it
O(n) time complexity, O(n) space complexity |

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
| 4 | [Middle of Linked List](https://leetcode.com/problems/middle-of-the-linked-list/description/) | slow and fast pointer|
| 5 | [LRU cache](https://leetcode.com/problems/lru-cache/) | keep mru in the tail and lru in the head,
keep dummy head and tail to avoid edge cases
if key exits, remove the node and add new node to the tail |

### **🌳 Trees**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Level Order Traversal](https://leetcode.com/problems/binary-tree-level-order-traversal/) | bfs, for each node, add its children and current level + 1 to the queue,
 and use hashmap to keep track of node values at each level |
| 2 | [Right Side View](https://leetcode.com/problems/binary-tree-right-side-view/) | DFS: if dfs right child first starting with level 0, at each level append to result the first node visited -> len(result) == depth, BFS: loop through the queue at each level, the last element is the rightmost |
| 3 | [Good Nodes](https://leetcode.com/problems/count-good-nodes-in-binary-tree/description/) | keep track of max in dfs and count when max is updated, start with the root value |
| 4 | [Validate BST](https://leetcode.com/problems/validate-binary-search-tree/) | validate each node, and the subtree as well, so set a range for each dfs call, right -> node.val is min, left -> node.val is max |
| 5 | [Kth Smallest Element in a BST](https://leetcode.com/problems/kth-smallest-element-in-a-bst/) | inorder traversal of bst gives sorted elements, can keep a decreasing counter after left dfs for more efficient solution |
| 6 | [Binary Tree from in-order and pre-order traversal](https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/) | for each node in preorder, split the inorder into two halves and recurse, use hashmap to store inorder indexes, use left and right pointers for slices of splits | 


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
| 10 | [Course Schedule](https://leetcode.com/problems/course-schedule/description/) | detect cycle with dfs for each node, build adjacency list using the prerequisites list, memoize for nodes by emptying prereqs for nodes that return True |
| 11 | [Accounts Merge](https://leetcode.com/problems/accounts-merge/) | build an adjacency list from the given accounts, each email is a node
dfs traversal through each email to find al connected emails, treat the path as emails of a single person |

### **🌀 Backtracking**  
| # | Problem | Notes |
|---|---------|-------|
| 1 | [Subsets](https://leetcode.com/problems/subsets) | for each element, either include it in subset or not, gives series of actions for 2^n subsets for n elements; backtracking: popping recently added element |
| 2 | [Combination Sum](https://leetcode.com/problems/combination-sum/description/) | build a decision tree out of the possible actions at each element, each action can be a recursion to i+1 element with append and after pop |
| 2 | [Combination Sum II](https://leetcode.com/problems/combination-sum-ii/description/) | build a decision tree out of the possible actions at each element, first sort to avoid repeated runs, and in each recursion after popping, check for duplicates|

| 3 | [Permutations](https://leetcode.com/problems/permutations/) | recurse for each element, keep track of visited element for each recursion level to avoid duplicates, backtrack/pop after returning the dfs |
| 4 | [Subsets II](https://leetcode.com/problems/subsets-ii/) | in the subsets with unique elements problem, just add while loop to skip duplicates
time: O(n*2^n), space: O(n) |
| 5 | [Generate Parentheses](https://leetcode.com/problems/generate-parentheses/) | Don't get anxious about stacks, think of them as a data structure to look backwards
keep a count of open and close parentheses,
if open remains, add open and recurse,
backtrack and check if close can be added; close<open
if open == close == n, add to result |
| 6 | [Word Search](https://leetcode.com/problems/word-search/) | go through each cell, compare the letter with the each subsequent letter in the word,
if match, look in the other directions, with a visited set to avoid going back
increment index of word while recursing,
remember: mutable objects are passed by reference, so remove the cell from visited set when backtracking |


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
| 6 | [Longest Palindromic Substring](https://leetcode.com/problems/longest-palindromic-substring/description/) | 2P: two pointers: treat each character as a center and expand outwards, with odd and even approaches ,  DP O(n^2) time and O(n^2) space: start from the end, keep 2d array updated for left,right, update result if palindrome and >max |
| 7 | [Palindromic Substrings](https://leetcode.com/problems/palindromic-substrings/description/) | Dynamic Programming: O(n^2) => substring is palindrome if substring i+1, j-1 is palindrome,
 Iterative 2P: O(n^2) => expand around center to count odd and even length palindromes | 
| 8 | [Decode Ways](https://leetcode.com/problems/decode-ways/) | TD: build decision tree, if end reached return 1 else 0, accumulate the counts, BU: one char: i= sum of i-1, two char: sum of i-2 since you take two characters, accumulate on no of ways from two characters back |
| 9 | [Coin Change](https://leetcode.com/problems/coin-change/description/) | TD approach:
recursion will return the number of coins used at each step, return 0 when target met,
add 1 to each return at the seceding step
if the main function returns float("inf"), return -1
BU approach:
create a table for all amounts from 0 to target
for each amount, loop through all coins, for each coin, find the no of coins needed minus the amount and add one coin |
| 10 | [Max Subarray](https://leetcode.com/problems/maximum-subarray/) | kadane's algorithm: discard previous sum if it is less than current number
O(n) time complexity, O(1) space complexity |
| 11 | [Max Product Subarray](https://leetcode.com/problems/maximum-product-subarray/) | keep track of negative numbers as well, record the max and min at each iteration,
update max_product with max of max_product, min product and max at each iteration |
| 12 | [Word Break](https://leetcode.com/problems/word-break/) | start from first character, word break valid only if starting with first,
loop through slices of string, if slice in word dict, recurse from that index
if end reached, return true
memoize the results for quick lookup |