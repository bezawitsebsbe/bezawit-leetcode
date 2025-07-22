# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Create a min-heap
        min_heap = []
        
        # Initialize the heap with the head of each linked list
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap, (lists[i].val, i, lists[i]))  # (value, index, node)
        
        dummy = ListNode(0)  # Dummy node to simplify result handling
        current = dummy
        
        while min_heap:
            # Extract the smallest node
            val, index, node = heapq.heappop(min_heap)
            current.next = node  # Link the smallest node to the merged list
            current = current.next  # Move to the next position
            
            # If the extracted node has a next node, push it into the heap
            if node.next:
                heapq.heappush(min_heap, (node.next.val, index, node.next))
        
        return dummy.next  # Return the head of the merged linked list

# Helper function to create a linked list from a list
def create_linked_list(elements):
    dummy = ListNode(0)
    current = dummy
    for val in elements:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Example usage
lists = [
    create_linked_list([1, 4, 5]),
    create_linked_list([1, 3, 4]),
    create_linked_list([2, 6])
]

solution = Solution()
merged_head = solution.mergeKLists(lists)

# Function to convert linked list back to list for easy comparison
def linked_list_to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

output = linked_list_to_list(merged_head)
print(output)  # Output should be [1, 1, 2, 3, 4, 4, 5, 6]
        