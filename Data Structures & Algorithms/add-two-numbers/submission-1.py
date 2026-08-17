# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0)
        temp1 = l1
        temp2 = l2
        prev = dummy
        
        while temp1 or temp2:
            n1 = temp1.val if temp1 else 0
            n2 = temp2.val if temp2 else 0
            sum = carry + n1 + n2
    
            carry = sum // 10
            new_node = ListNode(sum % 10) 
            prev.next = new_node
            prev = prev.next

            temp1 = temp1.next if temp1 else None
            temp2 = temp2.next if temp2 else None

        if carry > 0:
            prev.next = ListNode(carry)
        return dummy.next

            


        