# Python program to delete a given key from
# linked list.
"""
Input : 2->5->7->8->10->(head node)
        data = 5
Output : 2->7->8->10->(head node)

Input : 2->5->7->8->10->(head node)
         7
Output : 2->5->8->10->(head node)
"""

# Node of a doubly linked list
class Node:
    def __init__(self, next=None, data=None):
        self.next = next
        self.data = data

    # Function to insert a node at the beginning of


# a Circular linked list
def push(head_ref, data):
    # Create a new node and make head as next
    # of it.
    ptr1 = Node()
    ptr1.data = data
    ptr1.next = head_ref

    # If linked list is not None then set the
    # next of last node
    if (head_ref != None):

        # Find the node before head and update
        # next of it.
        temp = head_ref
        while (temp.next != head_ref):
            temp = temp.next
        temp.next = ptr1

    else:
        ptr1.next = ptr1  # For the first node

    head_ref = ptr1
    return head_ref


# Function to print nodes in a given
# circular linked list
def printList(head):
    temp = head
    if (head != None):
        while (True):
            print(temp.data, end=" ")
            temp = temp.next
            if (temp == head):
                break
    print()


# Function to delete a given node from the list
def deleteNode(head, key):
    # If linked list is empty
    if head is None:
        return -1

    # if the data is head
    if head.data == key:
        return None

    prevptr = None
    ptr = head
    while True:
        prevptr = ptr
        ptr = ptr.next
        if ptr.data == key:
            prevptr.next = ptr.next
            break
        else:
            print("no such keyfound")
            break

    return head

# Driver code

# Initialize lists as empty
head = None

# Created linked list will be 2.5.7.8.10
head = push(head, 2)
head = push(head, 5)
head = push(head, 7)
head = push(head, 8)
head = push(head, 10)

print("List Before Deletion: ")
printList(head)

head = deleteNode(head, 9)

print("List After Deletion: ")
printList(head)
