# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = list1
        temp2 = list2
        dummy = ListNode()
        curr = dummy
        while(temp1 and temp2):
            if temp1.val<temp2.val:
                node = ListNode(temp1.val)
                curr.next = node
                curr = curr.next
                temp1 = temp1.next
            else:
                node = ListNode(temp2.val)
                curr.next = node
                curr = curr.next
                temp2 = temp2.next
        while(temp1):
            node = ListNode(temp1.val)
            curr.next = node
            curr = curr.next
            temp1 = temp1.next
        while(temp2):
            node = ListNode(temp2.val)
            curr.next = node
            curr = curr.next
            temp2 = temp2.next
        return dummy.next