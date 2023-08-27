# The Celebrity Problem
"""A celebrity is a person who is known to all but does not know anyone at a party. If you go to a party of N people,
find if there is a celebrity in the party or not.
A square NxN matrix M[][] is used to represent people at the party such that
if an element of row i and column j  is set to 1 it means ith person knows jth person.
Here M[i][i] will always be 0.
Note: Follow 0 based indexing.
Follow Up: Can you optimize it to O(N)
Input:
N = 3
M[][] = {{0 1 0},
         {0 0 0},
         {0 1 0}}
Output: 1
Explanation: 0th and 2nd person both
know 1. Therefore, 1 is the celebrity.


"""


# User function Template for python3

class Solution:

    # Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        for i in range(n):
            count = 0
            for j in range(n):
                if i != j and M[j][i] == 1 and M[i][j] == 0:
                    count += 1
            if count == n - 1:
                return i
        return -1


# code here


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().strip().split()))
        k = 0
        m = []
        for i in range(n):
            row = []
            for j in range(n):
                row.append(a[k])
                k += 1
            m.append(row)
        ob = Solution()
        print(ob.celebrity(m, n))
# } Driver Code Ends
