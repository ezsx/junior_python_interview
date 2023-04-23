# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def get_int_from_tree(cur_node):
    str_number = ""
    while cur_node is not None:
        str_number += f"{cur_node.val}"
        cur_node = cur_node.next
    str_number = str_number[::-1]
    return int(str_number)


def create_linked_list_from_number(s):
    int_list = [int(char) for char in s]
    head = ListNode(int_list[0])
    current = head
    for i in range(1, len(int_list)):
        node = ListNode(int_list[i])
        current.next = node
        current = node
    return head


class Solution:
    def addTwoNumbers(self, l1: [ListNode], l2: [ListNode]) -> [ListNode]:
        return create_linked_list_from_number(str((get_int_from_tree(l1) + get_int_from_tree(l2)))[::-1])
