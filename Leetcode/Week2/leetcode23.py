def mergeKLists(lists):
    def merge(lst1, lst2):
        dummy = pt = ListNode(-1)
        while lst1 and lst2:
            if lst1.val < lst2.val:
                pt.next = lst1
                lst1 = lst1.next
            else:
                pt.next = lst2
                lst2 = lst2.next
            pt = pt.next

        pt.next = lst1 if not lst2 else lst2
        return dummy.next

    if not lists:
        return None

    if len(lists) == 1:
        return lists[0]
    mid = len(lists) / 2
    left = mergeKLists(lists[:mid])#这是调用了大函数 然后就非常棒了。
    right = mergeKLists(lists[mid:])#二分的思想，一直递归到最原始

    return merge(left, right)

from functools import reduce
# ---------------分而治之---
#b=reduce(mergeTwoLists,lists[1:],lists[0])  妙用迭代
def mergeKLists(self, lists):
    if not lists:
        return None

    sentinel = ListNode('0')
    while len(lists) > 1:
        merged = []
        while len(lists) > 1:
            merged.append(self.merge(lists.pop(), lists.pop(), sentinel))
        lists += merged
    return lists[0]


def merge(self, x, y, s):
    current = s
    while x and y:
        if x.val < y.val:
            current.next = x
            x = x.next
        else:
            current.next = y
            y = y.next
        current = current.next
    current.next = x if x else y
    return s.next
# ---------------分而治之---————————————————

from queue import PriorityQueue
class Solution(object):
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        for node in lists:
            if node: q.put((node.val,node))
        while q.qsize()>0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next: q.put((curr.next.val, curr.next))
        return dummy.next

import heapq
def mergeKLists(self, lists):
    current = sentinel = ListNode(0)
    lists = [(i.val, i) for i in lists if i]#存储 更priorty 类似
    heapq.heapify(lists)#排序
    while lists:
        current.next = heapq.heappop(lists)[1] #取第一个元素
        current = current.next
        if current.next:
            heapq.heappush(lists, (current.next.val, current.next))
    return sentinel.next



from operator import attrgetter

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        sorted_list = []
        for head in lists:
            curr = head
            while curr is not None:
                sorted_list.append(curr)
                curr = curr.next

        sorted_list = sorted(sorted_list, key=attrgetter('val'))
        for i, node in enumerate(sorted_list):
            try:
                node.next = sorted_list[i + 1]
            except:
                node.next = None

        if sorted_list:
            return sorted_list[0]
        else:
            return None



from heapq import heappush, heappop, heapreplace, heapify
class Solution(object):

    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        h = [(n.val, n) for n in lists if n]
        heapify(h)
        while h:
            val, node = h[0]  #弹出最小的值
            if not node.next:
                heappop(h)  #弹出最后了
            else:
                heapreplace(h, (node.next.val, node.next)) #  在出堆的同时入堆 非常好，
            cur.next = node
            cur = cur.next
        return dummy.next