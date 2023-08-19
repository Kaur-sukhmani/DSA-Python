# Implement two stacks in an array
"""
Your task is to implement  2 stacks in one array efficiently. You need to implement 4 methods.
push1 : pushes element into first stack.
push2 : pushes element into second stack.
pop1 : pops element from first stack and returns the popped element. If first stack is empty, it should return -1.
pop2 : pops element from second stack and returns the popped element. If second stack is empty, it should return -1.



Input:
push1(2)
push1(3)
push2(4)
pop1()
pop2()
pop2()
Output:
3 4 -1
Explanation:
push1(2) the stack1 will be {2}
push1(3) the stack1 will be {2,3}
push2(4) the stack2 will be {4}
pop1()   the poped element will be 3 from stack1 and stack1 will be {2}
pop2()   the poped element will be 4 from stack2 and now stack2 is empty
pop2()   the stack2 is now empty hence returned -1.
"""


# User function Template for python3

#User function Template for python3
class TwoStacks:
    def __init__(self, n=100):
        self.size = n
        self.arr = [0] * n
        self.top1 = -1
        self.top2 = n

    # Function to push an integer into stack 1
    def push1(self, x):
        self.top1 += 1
        self.arr[self.top1] = x
        pass
    # Function to push an integer into stack 2
    def push2(self, x):
        self.top2 -= 1
        self.arr[self.top2] = x
        pass

    # Function to remove an element from top of stack 1
    def pop1(self):
        if (self.top1== -1):
            return -1
        ans = self.arr[self.top1]
        self.arr[self.top1] = 0
        self.top1 -= 1
        return ans
        pass

    # Function to remove an element from top of stack 2
    def pop2(self):
        if (self.top2 == self.size):
            return -1
        ans = self.arr[self.top2]
        self.arr[self.top2] = 0
        self.top2 += 1
        return ans
        pass

#{
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    while T > 0:
        sq = TwoStacks()
        Q = int(input())
        while Q > 0:
            query = list(map(int, input().split()))
            if query[1] == 1:
                if query[0] == 1:
                    sq.push1(query[2])
                elif query[0] == 2:
                    sq.push2(query[2])
            elif query[1] == 2:
                if query[0] == 1:
                    print(sq.pop1(), end=' ')
                elif query[0] == 2:
                    print(sq.pop2(), end=' ')
            Q -= 1
        print()
        T -= 1

# } Driver Code Ends
