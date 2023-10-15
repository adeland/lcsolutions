class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
      
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        remove = n * -1 
        elements = []
        current = head

        while current != None:
            elements.append(current.val)
            current = current.next
        
        elements.pop(remove)

        if len(elements) > 0:
            head = ListNode(elements[0])
            current = head
            for node in elements[1:]:
                current.next = ListNode(node)
                current = current.next
              
            return head
