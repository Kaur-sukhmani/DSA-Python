# User function Template for python3
# FLOYD'S DETECTION ALGORITHM
"""
# Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

"""


class Solution:
    # Function to check if the linked list has a loop.

    def detectloop(self, head):
        if head is None:
            return False
        else:
            slow = head
            fast = head

            while fast is not None and fast.next is not None:
                slow = slow.next
                fast = fast.next.next

                if slow == fast:
                    return True

            return False


"""
    ==============TIME LIMIT EXCEEDED==================
     if head is None:
            return False
        elif head.next is head:
            return True
        else:
            temp = head
            temp_list = []
            while True:
                if temp not in temp_list:
                    temp_list.append(temp)
                    temp = temp.next

                    if temp is None:
                        return False
                else:
                    return True

"""
"""
*******************IMPORTANT******************
Floyd's cycle detection algorithm, also known as the "tortoise and the hare" algorithm. 
     'This algorithm allows us to detect a cycle in a linked list using two pointers moving at different speeds.

"""


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    # creates a new node with given value and appends it at the end of the linked list
    def insert(self, val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

    # connects last node to node at position pos from begining.
    def loophere(self, pos):
        if pos == 0:
            return

        walk = self.head
        for i in range(1, pos):
            walk = walk.next

        self.tail.next = walk


if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())

        LL = LinkedList()
        for i in input().split():
            LL.insert(int(i))

        LL.loophere(int(input()))

        print(Solution().detectloop(LL.head))
# } Driver Code Ends
