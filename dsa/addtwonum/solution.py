from typing import Optional
from addtwonum.listnode import ListNode


class Solution:
    def __init__(self):
        pass
    
    def addTwoNumbers(self,l1:Optional[ListNode],l2:Optional[ListNode])->Optional[ListNode]:
        dummy=ListNode(0)
        current=dummy
        carry=0
        while l1 or l2 or carry:
            total=carry
            if(l1):
                total+=l1.val
                l1=l1.next
            if(l2):
                total+=l2.val
                l2=l2.next
            carry,digit=divmod(total,10)
            current.next=ListNode(digit)
            current=current.next
        return dummy.next
                
            
