# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # merge first two lists into first head
        # for i in range(1,len(lists)):
        #     temp1 = lists[0]
        #     temp2 = lists[i]
        #     prev = temp1
        #     while(temp1 and temp2):
        #         if temp1.val<temp2.val:
        #             temp1 = temp1.next
        #             prev = temp1
        #         else:
        #             next1 = temp1.next
        #             next2 = temp2.next
        #             temp1.next = temp2
        #             temp2.next = next1

        #             prev = temp2
        #             temp1 = temp1.next.next
        #             temp2 = next2
        #     if temp2:
        #         prev = temp2
        #     if temp1:
        #         continue
        
        # return lists[0]
        if not lists:
            return None
        l = []
        for ll in lists:
            t = ll
            while(t):
                l.append(t)
                t = t.next
        l.sort(key = lambda t : t.val)
        # print(l)
        for i in range(len(l)-1):
            l[i].next = l[i+1]
        l[-1].next = None
        return l[0]


















