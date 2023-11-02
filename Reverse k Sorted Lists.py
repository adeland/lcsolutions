class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        elements = []

        for node in lists:
            current = node
            while current != None:
                elements.append(current.val)
                current = current.next

        elements = sorted(elements)

        if len(elements) > 0:
            head = ListNode(elements[0])
            current = head
            for node in elements[1:]:
                current.next = ListNode(node)
                current = current.next
            return head

