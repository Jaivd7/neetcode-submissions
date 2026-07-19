# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 and list2:
            if list1.val >= list2.val:
                temp = list2.next
                list1 = self.mergeTwoLists(list1, temp)
                list2.next = list1
                return list2
            else:
                temp = list1.next
                list2 = self.mergeTwoLists(list2, temp)
                list1.next = list2
                return list1
        elif not list1:
            return list2
        elif not list2:
            return list1
        else:
            return None