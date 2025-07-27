# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head or not head.next:
            return
        
        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: Reverse the second half of the list
        prev = None
        current = slow
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        # Step 3: Merge the two halves
        first, second = head, prev  # 'second' is the head of the reversed second half
        while second:
            # Save the next nodes
            temp1 = first.next
            temp2 = second.next
            
            # Rearrange pointers
            first.next = second
            second.next = temp1
            
            # Move to the next nodes
            first = temp1
            second = temp2
        
        # Optionally, set the last node's next to None to avoid any potential cycles
        if first:
            first.next = None