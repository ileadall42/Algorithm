def swapPairs(self, head):
    pre, pre.next = self, head
    while pre.next and pre.next.next:
        a = pre.next
        b = a.next
        pre.next, b.next, a.next = b, a, b.next
        pre = a
    return self.next


class Solution:
    # @param a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        p1 = guard = ListNode(0)
        guard.next = head

        try:
            while True:
                p0, p1, p2 = p1, p1.next, p1.next.next
                p0.next, p1.next, p2.next = p2, p2.next, p1#只需要改变指向就好了
        except:
            return guard.next


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x #z  最容易理解的一个
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        start = dummyHead
        while start.next is not None and start.next.next is not None:
            first, second = start.next, start.next.next
            start.next = second
            first.next = second.next##直接改变结点的指向就好当前位置就改变了 有一个dummy在永远不会被破坏
            second.next = first
            start = first
        return dummyHead.next



class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        new_head = head.next
        head.next = self.swapPairs(head.next.next)
        new_head.next = head
        return new_head# 递归版本

