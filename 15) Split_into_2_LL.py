# User function Template for python3

'''
class Node:
    def __init__(self):
        self.data = None
        self.next = None
'''


# def getSize(head):
#     res = 0

#     while head is not None:
#         head = head.next
#         res += 1
#     return res
class Solution:
    def findMid(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def splitList(self, head, head1, head2):
        if not head:
            return head1, head2

        mid = self.findMid(head)
        head1 = head
        head2 = mid.next
        mid.next = None

        return head1, head2
        # =========Runtime Error===========
        # n = getSize(head)
        # mid = int(n/2)
        # ptr = head
        # while mid:
        #     ptr = ptr.next
        #     mid -= 1
        # head2 = ptr.next
        # ptr.next = None

        # ptr2 = head2
        # while ptr2.next is head:
        #     ptr2 = ptr2.next
        # if ptr2.next is head:
        #     ptr2.next = None
        # this is to emulate pass by reference in python please don't delete below line.
        return head1, head2


# {
# Driver Code Starts
# Initial Template for Python 3


class Node:
    def __init__(self):
        self.data = None
        self.next = None


def printCircularLinkedList(head):
    tmp = head
    while True:
        print(tmp.data, end=" ")
        tmp = tmp.next
        if tmp == head:
            break
    print()


if __name__ == "__main__":
    for i in range(int(input())):
        head = Node()
        head1 = Node()
        head2 = Node()
        tmp = head
        n = int(input())
        for i in input().split():
            tmp.next = Node()
            tmp = tmp.next
            tmp.data = int(i)
        head = head.next
        tmp.next = head
        obj = Solution()
        head1, head2 = obj.splitList(head, head1, head2)
        printCircularLinkedList(head1)
        printCircularLinkedList(head2)

# } Driver Code Ends