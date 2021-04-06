# encoding: utf-8
# @author: fengr358
# @time: 2021/4/3 23:49
# @desc:

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head:
            print ('start' + str(head.val))
        if head is None or head.next is None:
            return head
        new_order = self.reverseList(head.next)
        # if new_order:
        print('start&&&&&&' + str(head.val))
        print (new_order.val)
        new_order.next = head
        head.next = None


list_input = [1, 2, 3, 4, 5]
head = None
head_flag = head
for item in list_input:
    node = ListNode(item)
    if head is None:
        head = node
        head_flag = node
    else:
        head.next = node
        head = head.next

process = Solution().reverseList(head_flag)
# print (head_flag.val)
# print (head.val)
# process = head_flag
while process:
    print (process.val)
    process = process.next