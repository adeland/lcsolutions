class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = None
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        x = []
        current = head
        while current != None:
            x.append(current.val)
            current = current.next
        x = x[::-1]
        if len(x) > 0:
            head = ListNode(x[0])
            current = head
            for i in x[1:]:
                current.next = ListNode(i)
                current = current.next
            return head
