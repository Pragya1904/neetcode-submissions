# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_length(self, head: Optional[ListNode]) -> int:
        temp = head
        length = 0
        while temp:
            temp = temp.next
            length += 1
        
        return length
    
    def reverse(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # Initialize prev as None
        curr = head  # Start with curr at the head of the list

        while curr:
            temp = curr.next  # Store the next node
            curr.next = prev  # Reverse the pointer
            prev = curr       # Move prev forward
            curr = temp      # Move curr forward

        return prev  # prev is the new head of the reversed list


    def reorderList(self, head: Optional[ListNode]) -> None:

        if head is None or head.next is None:
            return
        dummy = ListNode(0)
        dummy.next = head

        length = self.find_length(head)

        mid_length = length // 2 if length % 2 == 0 else length // 2 + 1
        print(f"mid {mid_length}")
        slow = head
        fast = head
        
        while mid_length > 0:
            slow = fast
            fast = fast.next
            mid_length -= 1
        
        slow.next = None
        head2 = self.reverse(fast)
        if head2 is None:
            return
        temp = dummy

        for i in range(length):
            if i % 2 == 0:
                temp.next = head
                head = head.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        
        head = dummy.next



        