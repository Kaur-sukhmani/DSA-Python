# User function Template for python3

''' structure of node:

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

'''


def findIntersection(head1, head2):
    # return head
    head1_ptr = head1
    head2_ptr = head2
    intersection = None
    tail = None  # Pointer to keep track of the tail of the intersection list

    while head1_ptr is not None and head2_ptr is not None:
        if head1_ptr.data == head2_ptr.data:
            new_node = Node(head1_ptr.data)  # Create a new node for intersection

            if intersection is None:
                intersection = new_node
                tail = intersection
            else:
                tail.next = new_node
                tail = tail.next

            head1_ptr = head1_ptr.next
            head2_ptr = head2_ptr.next

        elif head1_ptr.data > head2_ptr.data:
            head2_ptr = head2_ptr.next

        else:
            head1_ptr = head1_ptr.next

    return intersection
    # head1_ptr = head1
    # head2_ptr = head2
    # intersection = None

    # while head1_ptr is not None and head2_ptr is not None:
    #     if head1_ptr.data == head2_ptr.data:
    #         if intersection is None:
    #             intersection = Node(head1_ptr.data)
    #         else:
    #             intersection.next = Node(head1_ptr.data)
    #             intersection = intersection.next

    #         head1_ptr = head1_ptr.next
    #         head2_ptr = head2_ptr.next

    #     elif head1_ptr.data > head2_ptr.data:
    #         head2_ptr = head2_ptr.next

    #     else:
    #         head1_ptr = head1_ptr.next

    # return intersection
    # head1_ptr = head1
    # head2_ptr = head2
    # intersection = None

    # while (head1_ptr.next is not None) and (head1_ptr.next is not None):
    #     if (head1_ptr.data == head2_ptr.data):
    #         if intersection is None:
    #             intersection = head1_ptr.data
    #             intersection.next = None
    #         else:
    #             intersection.next = head1_ptr.data
    #             head1_ptr.next = None

    #         head1_ptr = head1_ptr.next
    #         head2_ptr = head2_ptr.next

    #     elif head1_ptr.data > head2_ptr.data :
    #         head2_ptr = head2_ptr.next

    #     else:
    #         head1_ptr = head1_ptr.next
    # return intersection


# {
# Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, data):
        if self.head is None:
            self.head = Node(data)
            self.tail = self.head
        else:
            self.tail.next = Node(data)
            self.tail = self.tail.next


def printList(head):
    while head:
        print(head.data, end=' ')
        head = head.next


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):

        n1, n2 = [int(x) for x in input().split()]
        arr1 = [int(x) for x in input().split()]
        ll1 = linkedList()
        for i in arr1:
            ll1.insert(i)

        arr2 = [int(x) for x in input().split()]
        ll2 = linkedList()
        for i in arr2:
            ll2.insert(i)

        result = findIntersection(ll1.head, ll2.head)
        printList(result)
        print()

# } Driver Code Ends