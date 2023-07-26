"""
We have discussed Floyd’s loop detection algorithm. Below are steps to find the first node of the loop.
1. If a loop is found, initialize a slow pointer to head, let fast pointer be at its position.
2. Move both slow and fast pointers one node at a time.
3. The point at which they meet is the start of the loop.
"""


# Python3 program to return first node of loop.
class Node:

    def __init__(self, key):
        self.key = key
        self.next = None


def newNode(key):
    temp = Node(key)
    return temp


# A utility function to print a linked list
def printList(head):
    while (head != None):
        print(head.key, end=' ')
        head = head.next

    print()


# Function to detect and remove loop
# in a linked list that may contain loop
def detectAndRemoveLoop(head):
    # If list is empty or has only one node
    # without loop
    if (head == None or head.next == None):
        return None

    slow = head
    fast = head

    # Move slow and fast 1 and 2 steps
    # ahead respectively.
    slow = slow.next
    fast = fast.next.next

    # Search for loop using slow and
    # fast pointers
    while (fast and fast.next):
        if (slow == fast):
            break

        slow = slow.next
        fast = fast.next.next

    # If loop does not exist
    if (slow != fast):
        return None

    # If loop exists. Start slow from
    # head and fast from meeting point.
    slow = head

    while (slow != fast):
        slow = slow.next
        fast = fast.next

    return slow


# Driver code
if __name__ == '__main__':

    head = newNode(50)
    head.next = newNode(20)
    head.next.next = newNode(15)
    head.next.next.next = newNode(4)
    head.next.next.next.next = newNode(10)

    # Create a loop for testing
    head.next.next.next.next.next = head.next.next

    res = detectAndRemoveLoop(head)

    if (res == None):
        print("Loop does not exist")
    else:
        print("Loop starting node is " +
              str(res.key))

# This code is contributed by rutvik_56
