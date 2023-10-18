class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        value1 = []
        value2 = []
        current1 = l1
        current2 = l2

        while current1 != None:
            value1.append(str(current1.val))
            current1 = current1.next

        while current2 != None:
            value2.append(str(current2.val))
            current2 = current2.next

        value1 = "".join(value1[::-1])
        value2 = "".join(value2[::-1])
        addedValue = str(int(value1) + int(value2))[::-1]
        ret = ListNode(addedValue[0])
        current = ret

        for value in addedValue[1:]:
            current.next = ListNode(value)
            current = current.next
        return ret

