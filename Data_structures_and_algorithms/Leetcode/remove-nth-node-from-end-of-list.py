# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def LN_to_arr(head):
    arr=[]
    current = head
    while current != None:
        arr.append(current.val)
        current=current.next
    return arr

def arr_to_LN(arr):
    LN = ListNode(val=arr[0])
    head = LN
    current = LN
    for el in arr[1:]:
        current.next = ListNode(val=el)
        current = current.next
    return head

class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        arr = LN_to_arr(head)
        print(arr)
        del arr[-n]
        print(arr)
        LN = arr_to_LN(arr)
        return LN

