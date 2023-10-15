class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = None
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        merged = []
        current = list1
        current2 = list2
        
        while current != None:
            merged.append(current.val)
            current = current.next

        while current2 != None:
            merged.append(current2.val)
            current2 = current2.next

        merged = sorted(merged)

        if len(merged) > 0:
            head = ListNode(merged[0])
            current = head
            for i in merged[1:]:
                current.next = ListNode(i)
                current = current.next
            return head

