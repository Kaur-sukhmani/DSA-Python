""" Ques: Union of two arrays
BasicAccuracy: 42.22%Submissions: 305K+Points: 1
Join the most popular course on DSA. Master Skills & Become Employable by enrolling today! 
Given two arrays a[] and b[] of size n and m respectively. 
The task is to find the number of elements in the union between these two arrays.

Union of the two arrays can be defined as the set containing distinct elements from both the arrays. 
If there are repetitions, then only one occurrence of element should be printed in the union.

Note : Elements are not necessarily distinct."""

#User function Template for python3

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        
        #code here
        set_a = set(a)
        set_b = set(b)
        
        # Find the union of the sets
        union_set = set_a.union(set_b)
        
        # Convert the result back to a list
        union_list = list(union_set)
        
        return len(union_list)
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
# } Driver Code Ends
