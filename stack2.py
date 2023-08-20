# Design a stack with operations on middle element
"""How to implement a stack which will support the following operations in O(1) time complexity?
1) push() which adds an element to the top of stack.
2) pop() which removes an element from top of stack.
3) findMiddle() which will return middle element of the stack.
4) deleteMiddle() which will delete the middle element.
Push and pop are standard stack operations.

Method 1:
The important question is, whether to use a linked list or array for the implementation of the stack?
Please note that we need to find and delete the middle element. Deleting an element from the middle is not O(1) for the array.
 Also, we may need to move the middle pointer up when we push an element and move down when we pop().
 In a singly linked list, moving the middle pointer in both directions is not possible.
The idea is to use a Doubly Linked List (DLL). We can delete the middle element in O(1) time by maintaining mid pointer.
 We can move the mid pointer in both directions using previous and next pointers.
Following is implementation of push(), pop() and findMiddle() operations.
If there are even elements in stack,
 findMiddle() returns the second middle element. For example, if stack contains {1, 2, 3, 4}, then findMiddle() would return 3.
"""


class DLLNode:

    def __init__(self, d):
        self.prev = None
        self.data = d
        self.next = None


class myStack:

    def __init__(self):
        self.head = None
        self.mid = None
        self.count = 0


def createMyStack():
    ms = myStack()
    ms.count = 0
    return ms


def push(ms, new_data):
    new_DLLNode = DLLNode(new_data)
    new_DLLNode.prev = None
    new_DLLNode.next = ms.head
    ms.count += 1

    if ms.count == 1:
        ms.mid = new_DLLNode

    else:
        ms.head.prev = new_DLLNode

        # Update mid if ms->count is odd
        if (ms.count % 2) != 0:
            ms.mid = ms.mid.prev
    ms.head = new_DLLNode


def pop(ms):
    if (ms.count == 0):
        print("Stack is empty")
        return -1
    temp = ms.head.next
    temp.prev = None
    ms.head = temp
    ms.count -= 1
    if ((ms.count % 2) != 0):
        ms.mid = ms.mid.prev
    return ms.head.data


def findMiddle(ms):
    if (ms.count == 0):
        print("stack is empty")
        return
    return ms.mid.data


def deleteMiddle(ms):
    if (ms.count == 0):
        print("Stack is empty now")
        return
    ms.count -= 1
    ms.mid.next.prev = ms.mid.prev
    ms.mid.prev.next = ms.mid.next

    if ms.count % 2 == 1:
        ms.mid = ms.mid.next
    else:
        ms.mid = ms.mid.prev


if __name__ == '__main__':
    ms = createMyStack()
    push(ms, 11)
    push(ms, 22)
    push(ms, 33)
    push(ms, 44)
    push(ms, 55)
    push(ms, 66)
    push(ms, 77)
    push(ms, 88)
    push(ms, 99)

    print("Popped : " +
          str(pop(ms)))
    print("Popped : " +
          str(pop(ms)))
    print("Middle Element : " +
          str(findMiddle(ms)))
    deleteMiddle(ms)
    print("New Middle Element : " +
          str(findMiddle(ms)))
