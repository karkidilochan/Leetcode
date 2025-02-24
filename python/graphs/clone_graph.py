"""
my solution: use bfs as its more efficient to traverse one level at a time, and avoid deep recursion
1. create a dictionary to store the adjacency list of the graph
2. with a queue, create a new node for each node in the graph
3. add the neighbors of the current node to the queue only if they are not already in the adjacency list
4. if they are in the adjacency list, add the current node to the neighbors of the node in the adjacency list
5. return the node with value 1 from the adjacency list

-> neetcode solution: use a hashmap to keep track of clones of each visited node, 
with bfs, for each node, create a new node, add it to the hashmap, and add its neighbors to the queue
for its neighbors, add their clones to the clone of current node
"""

from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        from collections import deque, defaultdict

        if not node:
            return node
        adj_list = defaultdict(list)
        queue = deque([node])
        while queue:
            curr = queue.pop()
            if curr.val not in adj_list:
                new_curr = Node(curr.val)
                adj_list[curr.val] = new_curr
                neighbors = curr.neighbors
                for ne in neighbors:
                    if ne.val in adj_list:
                        adj_list[ne.val].neighbors.append(new_curr)
                        adj_list[curr.val].neighbors.append(adj_list[ne.val])
                    else:
                        queue.appendleft(ne)
        return adj_list[1]
