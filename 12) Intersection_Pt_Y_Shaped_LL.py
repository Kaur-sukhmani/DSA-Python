"""Input:
Linked List 1 = 4->1->common
Linked List 2 = 5->6->1->common
common = 8->4->5->NULL
Output: 8
Explanation:

4              5
|              |
1              6
 \             /
  8   -----  1
   |
   4
   |
  5
  |
  NULL
  """
# User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.

	Function Arguments: head_a, head_b (heads of both the lists)

	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

# User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.

	Function Arguments: head_a, head_b (heads of both the lists)

	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''


# Function to find intersection point in Y shaped Linked Lists.

def getSize(head):
    res = 0

    while head is not None:
        head = head.next
        res += 1
    return res


# Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1, head2):
    n1 = getSize(head1)

    # finding length of list2.
    n2 = getSize(head2)

    # if list1 is longer, we ignore some of its starting
    # elements till it has as many elements as list2.
    while n1 > n2:
        head1 = head1.next
        n1 -= 1

    # similarly, if list2 is longer, we ignore some of its starting
    # elements till it has as many elements as list1.
    while n2 > n1:
        head2 = head2.next
        n2 -= 1

    # now we simply traverse ahead till we get the intersection point, if there
    # is none, this loop will break when both pointers point at NULL.
    while head1 != head2:
        head1 = head1.next
        head2 = head2.next

    # if head1 is not NULL, we return its data otherwise we return -1.
    if head1 is not None:
        return head1.data
    return -1
    # ===========not for large data vaise sahi tha======
    # ptr1 = head1
    # ptr2 = head2

    # while(ptr1.next != None and ptr2.next != None):
    #     if (ptr1.data == ptr2.data):
    #         return ptr1.data

    #     elif (ptr1.data < ptr2.data):
    #         ptr1 = ptr1.next

    #     else:
    #         ptr2 = ptr2.next

    # return -1


# {
# Driver Code Starts
# Initial Template for Python 3

# Contributed by : Nagendra Jha

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


# Node Class
class Node:
    def __init__(self, data):  # data -> value stored in node
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        temp = None

    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_node):
        if self.head is None:
            self.head = new_node
            self.temp = self.head
            return
        else:
            self.temp.next = new_node
            self.temp = self.temp.next


if __name__ == '__main__':
    t = int(input())
    for cases in range(t):
        x, y, z = map(int, input().strip().split())
        a = LinkedList()  # create a new linked list 'a'.
        b = LinkedList()  # create a new linked list 'b'.
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        nodes_common = list(map(int, input().strip().split()))

        for x in nodes_a:
            node = Node(x)
            a.append(node)  # add to the end of the list

        for x in nodes_b:
            node = Node(x)
            b.append(node)  # add to the end of the list

        for i in range(len(nodes_common)):
            node = Node(nodes_common[i])
            a.append(node)  # add to the end of the list a
            if i == 0:
                b.append(node)  # add to the end of the list b, only the intersection

        print(intersetPoint(a.head, b.head))

# } Driver Code Ends