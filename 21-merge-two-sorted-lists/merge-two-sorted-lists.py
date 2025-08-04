# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy
        
        # Traverse both lists
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1  # Link the smaller node
                list1 = list1.next     # Move to the next node in list1
            else:
                current.next = list2  # Link the smaller node
                list2 = list2.next     # Move to the next node in list2
            current = current.next     # Move the current pointer
        
        # If there are remaining nodes in either list, link them
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        # The merged list starts from the next node of dummy
        return dummy.next
        