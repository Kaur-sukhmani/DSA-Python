# Given an array A of size N of integers. 
# Your task is to find the sum of minimum and maximum element in the array.

class Solution:
    def findSum(self,A,N): 
        #code here
        minimum = min(A)
        maximum = max(A)
        sum = minimum + maximum
        return sum 
        
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3



t=int(input())
for _ in range(0,t):
    n=int(input())
    a=list(map(int,input().split()))
    ob = Solution()
    print(ob.findSum(a,n))
# } Driver Code Ends
