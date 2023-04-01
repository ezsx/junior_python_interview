class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
node3 = ListNode(3)
node2 = ListNode(2, node3)
node1 = ListNode(1, node2)


def mergeTwoLists(list1: [ListNode], list2: [ListNode]) -> [ListNode]:
    dummy = ListNode()
    current = dummy

    while list1 and list2:
        if list1.val < list2.val:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    elif list2:
        current.next = list2

    return dummy.next


