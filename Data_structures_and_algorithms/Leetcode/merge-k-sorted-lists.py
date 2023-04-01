class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_linked_lists(list1, list2):
    if list1.val < list2.val:
        list_res = list1
        list1 = list1.next
    else:
        list_res = list2
        list2 = list2.next
    current_node = list_res
    while list1 is not None and list2 is not None:
        if list1.val < list2.val:
            current_node.next = list1
            list1 = list1.next
        else:
            current_node.next = list2
            list2 = list2.next
        current_node = current_node.next
    if list2 is not None:
        current_node.next = list2
    if list1 is not None:
        current_node.next = list1
    return list_res

