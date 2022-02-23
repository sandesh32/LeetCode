"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def __init__(self):
        self.visited={}
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return
        if node.val in self.visited:
            return self.visited[node.val]
        ans=Node(node.val)
        self.visited[node.val]=ans
        for nebs in node.neighbors:
            temp = self.cloneGraph(nebs)
            ans.neighbors.append(temp)
        return ans 