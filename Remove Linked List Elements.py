class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        removed = []
        current = head

        while current != None:
            if current.val != val:
                removed.append(current.val)
            current = current.next
        
        if len(removed) > 0:
            head = ListNode(removed[0])
            current = head

            for node in removed[1:]:
                current.next = ListNode(node)
                current = current.next
                
            return head
        
    
    
