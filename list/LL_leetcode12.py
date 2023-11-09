""" Partition List

Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

 

Example 1:


Input: head = [1,4,3,2,5,2], x = 3
Output: [1,2,2,4,3,5]
Example 2:

Input: head = [2,1], x = 2
Output: [1,2]"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before, after = ListNode(0), ListNode (0)
        before_curr, after_curr = before, after # we created 2 diff seperate linked lists
        while head:
            if head.val < x:
                before_curr.next, before_curr = head, head
            else:
                after_curr.next, after_curr = head, head
            head = head.next

        after_curr.next = None
        before_curr.next = after.next


        return before.next
        #  if head is None or head.next is None:
        #     return head
        # temp = head
        # main = None
        # previous = None
        # next_of_main = temp.next

        # # Finding the node with value x
        # while temp:
        #     if temp.val == x:
        #         main = temp
        #         break
        #     previous = temp 
        #     temp = temp.next 
        #     next_of_main = temp.next 
        
        
        
        # curr_node = head
        # while curr_node:
        #     if curr_node.val < main.val:
        #         new_node = curr_node.next 
        #         previous.next = curr_node
        #         curr_node.next = main
        #         curr_node = previous_node 
        #         new_node = curr_node 

        #     if curr_node.val > main.val:
        #         new_node = curr_node.next 
        #         curr_node.next = main.next 
        #         main.next = curr_node
        #         curr_node = next_of_main
        #         mew_node = curr_node 
            
        #     if curr_node == main:
        #         curr_node = curr_node.next 
            
        # return head
            

        
            


                

        
