"""
Input: 1->2->3->4->5
Output: 5->1->2->3->4

Input: 3->8->1->5->7->12
Output: 12->3->8->1->5->7
"""
# code to move the last item to front


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Function to add a node
    # at the beginning of Linked List
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # Function to print nodes in a
    # given linked list
    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.data, end=", ")
            tmp = tmp.next
        print()

    # Function to bring the last node to the front
    def moveToFront(self):
        ptr1 = self.head
        prev_ptr1 = None
        while ptr1.next is not None:
            prev_ptr1 = ptr1
            ptr1 = ptr1.next

# SWAPPING FIRST AND LAST ELEMENT

        # if ptr1.next is None :
        #     temp_last = ptr1
        #     temp = temp_first.next
        #     temp_last.next = temp
        #     temp_first.next = None
        #     prev_ptr1.next = temp_first
        #     self.head = temp_last

        if ptr1.next is None :
            ptr1.next = self.head
            prev_ptr1.next = None   # point the next of the second
                                    # last node to None

            # Make the last node as the first Node
            self.head = ptr1



if __name__ == '__main__':
    llist = LinkedList()

    # swap the 2 nodes
    llist.push(5)
    llist.push(4)
    llist.push(3)
    llist.push(2)
    llist.push(1)
    print("Linked List before moving last to front ")
    llist.printList()

    # Function call
    llist.moveToFront()
    print("Linked List after moving last to front ")
    llist.printList()

