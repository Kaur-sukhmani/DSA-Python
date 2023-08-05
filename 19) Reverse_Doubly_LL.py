# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
'''


def reverseDLL(head):
    # return head after reversing
    prev_node = None
    current_node = head

    while current_node:
        # Swap prev and next pointers of the current node
        temp = current_node.prev
        current_node.prev = current_node.next
        current_node.next = temp

        # Move to the next node
        prev_node = current_node
        current_node = current_node.prev

    # Update the head to point to the last node, which is now the new head after reversal
    head = prev_node
    return head


# {
# Driver Code Starts
# Initial Template for Python 3

# contributed by RavinderSinghPB
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def push(self, new_data, tail):
        if not self.head:
            self.head = Node(new_data)
            return self.head
        Nnode = Node(new_data)
        Nnode.prev = tail
        tail.next = Nnode
        return Nnode

    def printList(self, node):
        while (node is not None):
            print(node.data, end=' ')
            node = node.next


if __name__ == '__main__':
    t = int(input())

    for tcs in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        dll = DoublyLinkedList()
        tail = None

        for e in arr:
            tail = dll.push(e, tail)

        resHead = reverseDLL(dll.head)
        dll.printList(resHead)
        print()

# } Driver Code Ends
