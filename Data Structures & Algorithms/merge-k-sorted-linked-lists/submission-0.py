# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None
        if len(lists) == 1:
            return lists[0]
        
        def mergeTwoLists(list1, list2):
            if list1 is None:
                return list2
            if list2 is None:
                return list1
            if list1.val <= list2.val:
                list1.next = mergeTwoLists(list1.next, list2)
                return list1
            else:
                list2.next = mergeTwoLists(list1, list2.next)
                return list2

        curr = lists[0]
        for i in range(1,len(lists)):
            curr = mergeTwoLists(curr, lists[i])
        return curr