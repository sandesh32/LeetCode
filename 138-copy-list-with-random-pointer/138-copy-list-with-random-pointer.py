"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return
        d={}
        ptr=head
        ptr2=head
        while ptr:
            d[ptr]=Node(ptr.val)
            ptr=ptr.next
        while ptr2:
            if ptr2.next is not None:
                d[ptr2].next=d[ptr2.next]
            if ptr2.random is not None:
                d[ptr2].random=d[ptr2.random]
            ptr2=ptr2.next
        return d[head]