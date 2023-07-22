"""Return reference of new head of the reverse linked list
  The input list will have at least one element
  Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
  This is method only submission.
  You only need to complete the method.
"""


class Solution:
    def reverse(self, head, k):
        prev_group = None
        curr_group = head
        while curr_group is not None:
            prev = curr_group
            curr = curr_group.next
            for i in range(k - 1):
                if curr is None:
                    break
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            if prev_group is None:
                head = prev
            else:
                prev_group.next = prev
            curr_group.next = None
            prev_group = curr_group
            curr_group = curr

        return head


#         if head is None or head.next is None:
#             return head
#         else:
#             point = None
#             current1 = head
#             i = k
#             while current1 is not None:
#                 pointer = current1
#                 current = current1.next
#                 for i in range(k-1):
#                     if current is None:
#                         break
#                     temp = current.next
#                     current.next = pointer
#                     pointer = current
#                     current = temp
#                 if pointer is None:
#                     head = pointer
#                 else:
#                     point.next = pointer
#                 current1.next = None
#                 point = current1
#                 current1 = current
#
#             return head


# Code here


# {
# Driver Code Starts
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        # self.tail

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            # arr.append(str(temp.data))
            temp = temp.next
        print()


if __name__ == '__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = input()
        values = list(map(int, input().split()))
        for i in reversed(values):
            llist.push(i)
        k = int(input())
        new_head = LinkedList()
        ob = Solution()
        new_head = ob.reverse(llist.head, k)
        llist.head = new_head
        llist.printList()
        t -= 1

# } Driver Code Endsx