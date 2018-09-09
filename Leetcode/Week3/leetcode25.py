def reverseKGroup(self, head, k):
    dummy = jump = ListNode(0)
    dummy.next = l = r = head

    while True:
        count = 0
        while r and count < k:  # use r to locate the range
            r = r.next
            count += 1
        if count == k:  # if size k satisfied, reverse the inner linked list
            pre, cur = r, l
            for _ in range(k):
                cur.next, cur, pre = pre, cur.next, cur  # standard reversing  #对python的理解呀，动态赋值是同时进行的
            jump.next, jump, l = pre, l, r  # connect two k-groups
        else:
            return dummy.next



def not_same():
    a=2
    b=4
    a,b,c=3,a,b
    print(a)
    print(b)
    print(c)

def same():
    a=3
    b=a
    c=b
    print(a)
    print(b)
    print(c)


print(not_same())
print('this is same',same())