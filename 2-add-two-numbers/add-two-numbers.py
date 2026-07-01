# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp = ans
        carry = 0
        while l1 and l2:
            temp.next = ListNode()
            temp = temp.next
            a = l1.val
            b = l2.val

            if a+b+carry >=10:
                rem = (a+b+carry)%10
                carry = 1
                temp.val = rem
            else:
                temp.val = a+b+carry
                carry = 0
            
            l1 = l1.next
            l2 = l2.next
        while l1:
            temp.next = ListNode()
            temp = temp.next
            if l1.val + carry >= 10:
                rem = (l1.val+carry)%10
                carry = 1
                temp.val = rem
            else:
               temp.val = l1.val+carry
               carry = 0
            l1 = l1.next
        while l2:
            temp.next = ListNode()
            temp = temp.next
            if l2.val + carry >= 10:
                rem = (l2.val+carry)%10
                carry = 1
                temp.val = rem
            else:
               temp.val = l2.val+carry
               carry = 0
            l2 = l2.next
        if carry == 1:
            temp.next = ListNode()
            temp = temp.next
            temp.val = carry
            


        return ans.next


        