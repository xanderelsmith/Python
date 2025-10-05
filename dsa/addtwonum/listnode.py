
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        # This will print the whole linked list.
        res = []
        curr = self
        while curr:
            res.append(str(curr.val))
            curr = curr.next
        return " -> ".join(res)