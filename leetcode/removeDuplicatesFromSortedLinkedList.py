# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    """
    Method1: Naive
    Time complexity: O(n), given that n is the length of the linked list
    Space complexity: O(n), given that n is the sorted list we return
    """
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret_head = head
        while head:
            if head.next and head.next.val == head.val:
                    head.next = head.next.next
            else:
                head = head.next
        
        return ret_head
        