# User function Template for python3

'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''


# Function to delete a given node from the list
def deleteNode(head, key):
    # your code goes here
    curr = head
    while curr.next != head:
        if curr.next.data == key:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head


# Function to reverse the list
def reverse(head):
    # your code goes here
    last = head
    curr = head
    while last.next != head:
        last = last.next
    prev = last
    while curr != last:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    curr.next = prev

    cur = head
    while cur.next != head:
        cur.data, cur.next.data = cur.next.data, cur.data
        cur = cur.next
    """if not head:
        return None

    curNode = head
    prevNode = None



    while (curNode.next != head):
        nextNode = curNode.next
        curNode.next = prevNode
        curNode = nextNode
        prevNode = curNode



    curNode.next = prevNode
    head.next = curNode

    return curNode"""


# {
# Driver Code Starts
# Initial Template for Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push(data, prev):
    if prev == None:
        prev = Node(data)
        return prev
    tmp = Node(data)
    prev.next = tmp
    return tmp


def printList(head):
    flg = False
    tmp = head
    while flg == False or tmp != head:
        flg = True
        print(tmp.data, end=" ")
        tmp = tmp.next
    print()


if __name__ == "__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(i) for i in input().split()]
        delNode = int(input())

        head = Node(None)
        prev = head
        for i in arr:
            prev = push(i, prev)
        head = head.next
        prev.next = head
        deleteNode(head, delNode)
        reverse(head)
        printList(head)

# } Driver Code Ends