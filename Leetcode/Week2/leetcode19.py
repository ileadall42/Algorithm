class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = 0


def removeNthFromEnd(self, head, n):
    fast = slow = head
    for _ in range(n):
        fast = fast.next
    if not fast:
        return head.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next   #一直都是人家引用head  到了最后slow.next 才是真正 slow.next.next 改变到了head 内部next内存的指向
    return head


 def removeNthFromEnd2(self, head, n):
        def index(node):
            if not node:
                return 0
            i = index(node.next) + 1
            if i > n:
                node.next.val = node.val
            return i
        index(head)
        return head.next


 def removeNthFromEnd(self, head, n):
        def remove(head):
            if not head:
                return 0, head
            i, head.next = remove(head.next)
            return i+1, (head, head.next)[i+1 == n]
        return remove(head)[1]






a=ListNode(3)
print(a)