# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode(0)  # Dummy node to simplify the result list
        current = dummy_head
        carry = 0
        
        while l1 or l2 or carry:
            # Get the values from the current nodes of l1 and l2
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and carry
            total = val1 + val2 + carry
            carry = total // 10
            new_node = ListNode(total % 10)  # Create a new node with the digit
            
            # Move to the next node in the result list
            current.next = new_node
            current = current.next
            
            # Move to the next nodes in l1 and l2
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        
        return dummy_head.next  # Return the next of dummy head to skip the dummy node