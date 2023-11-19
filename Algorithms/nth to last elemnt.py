# Implement and algorthm to find the nth to last elemnt of a singly linked list
from LL_leetcode10 import LinkedList

def nthtoLast(ll, n):
    pointer1 = ll.head  #O(1)
    pointer2 = ll.head #O(1)
    for i in range(n): #O(N)
        if pointer2 is None: #O(1)
            return None
        pointer2 = pointer2.next
    
    while pointer2: #O(N)
        pointer1 = pointer1.next #O(1)
        pointer2 = pointer2.next  #O(1)
    return pointer1 #O(1)
 
customLL = LinkedList()
customLL.generate(10, 0, 90)
print(customLL)
print(nthtoLast(customLL, 5))