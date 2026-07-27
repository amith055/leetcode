# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or head.next == None or k==0: return head
        head1 = head
        l = 0
        while head1:
            head1 = head1.next
            l+=1
        k = k%l
        if k == 0: return head
        while k>0:
            h = head
            prev = None
            while head.next!=None:
                prev = head
                head = head.next
            prev.next = None
            head.next = h
            k-=1
        return head
        