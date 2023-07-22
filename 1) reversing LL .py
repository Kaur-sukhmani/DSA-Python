# function Template for python3

"""
# Node Class

class node:
    def __init__(self, data):
        self.data = value
        self.next = None

"""


class Solution:
    # Function to reverse a linked list.
    def reverselist(self, head):
        # Code here
        if head is None or head.next is None:
            return head
        else:
            pointer = head
            current = pointer.next
            while current is not None:
                temp = current.next
                current.next = pointer
                pointer = current
                current = temp

            head.next = None
            return pointer

# {
# Driver Code Starts
# Node Class
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next


def printlist(head):
    tmp = head
    while tmp:
        print(tmp.data, end=' ')
        tmp = tmp.next
    print()


if __name__ == '__main__':
    for i in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]

        lis = Linked_List()
        for i in arr:
            lis.insert(i)

        newhead = Solution().reverselist(lis.head)
        printlist(newhead)

# } Driver Code Ends
