from typing import List, Optional
import heapq

class ListNode:
    def __init__(self, val=0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        min_heap = []

        # Initializes the heap with the head of each list
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(min_heap, (l.val, i, l))

        dummy = ListNode()
        current = dummy

        while min_heap:
            val, i, node = heapq.heappop(min_heap)
            current.next = node
            current = current.next
            if node.next:
                heapq.heappush(min_heap, (node.next.val, i, node.next))

        return dummy.next
