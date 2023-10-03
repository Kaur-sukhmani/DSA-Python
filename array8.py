"""Kadane's Algorithm
MediumAccuracy: 36.28%Submissions: 783K+Points: 4
Join the most popular course on DSA. Master Skills & Become Employable by enrolling today! 
Given an array Arr[] of N integers.
Find the contiguous sub-array(containing at least one number) 
which has the maximum sum and return its sum.

"""
#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr,N):
        ##Your code here
        curr_sum = 0
        max_so_far = arr[0]
        for i in range(0, N):
            curr_sum = curr_sum + arr[i]
            if (max_so_far < curr_sum):
                max_so_far = curr_sum
            if (curr_sum<0):
                curr_sum = 0 
        return max_so_far


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math

 
def main():
        T=int(input())
        while(T>0):
            
            n=int(input())
            
            arr=[int(x) for x in input().strip().split()]
            
            ob=Solution()
            
            print(ob.maxSubArraySum(arr,n))
            
            T-=1


if __name__ == "__main__":
    main()
# } Driver Code Ends
