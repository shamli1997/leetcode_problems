# Definition for singly-linked list.
from typing import List, Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists)==0:
            return None
#         merge the linked list until it becomes a single list
        while len(lists) > 1:
            mergedList = []
#             we are operating on pairs of linked list hence incrementor is 2
            for i in range(0,len(lists),2):
                l1 = lists[i]
                l2 = lists[i+1] if (i+1) < len(lists) else None
                mergedList.append(self.merge2List(l1,l2))
            lists = mergedList
        return lists[0]
    
    def merge2List(self,l1,l2):
        dummy = ListNode()
        tail = dummy
        
        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next
            tail = tail.next
        if l1:
            tail.next = l1
        if l2:
            tail.next = l2
        return dummy.next

