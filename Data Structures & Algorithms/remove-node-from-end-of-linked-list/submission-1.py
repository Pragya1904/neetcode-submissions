# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or not head.next and n == 1:
            return None

        temp = head
        length = 0

        while temp:
            temp = temp.next
            length += 1

        k = length - n
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        curr = head

        while k > 0:
            prev = curr
            curr = curr.next
            k -= 1
        
        prev.next = curr.next
        curr.next = None

        return dummy.next
