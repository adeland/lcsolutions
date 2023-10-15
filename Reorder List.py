class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
   
        elements = []
        reordered = []
        count = -1
        currentNode = head

        while currentNode != None:
            elements.append(currentNode.val)
            currentNode = currentNode.next

        for i in range(len(elements)):
            if len(reordered) == len(elements):
                break
            reordered.append(elements[i])
            if len(reordered) == len(elements):
                break
            reordered.append(elements[count])
            count -= 1

        count = 0

        while head != None:
            head.val = reordered[count]
            head = head.next
            count += 1

            
