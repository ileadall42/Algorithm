# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = head = ListNode(0)
        while l1.next != None and l2.next != None:
            if l1.val < l2.val:
                head.next = l1.val
                l1 = l1.next
            else:
                head.next = l2.val
                l2 = l2.next
        head.next = l2
        return dummy.next


def stringToIntegerList(input):
    input = input.strip()
    input = input[1:-1]
    return [int(number) for number in input.split(",")]


def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr


def listNodeToString(node):
    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return result[:-2]


import sys


def own_readlines():
    for line in input():
        yield line.strip('\n')


def main():
    lines = own_readlines()
    while True:
        try:
            line = lines.next()
            l1 = stringToListNode(line)
            line = lines.next()
            l2 = stringToListNode(line)

            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()