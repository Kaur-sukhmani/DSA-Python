"""Alternate positive and negative numbers



Given an unsorted array Arr of N positive and negative numbers. 
Your task is to create an array of alternate positive and negative numbers
without changing the relative order of positive and negative numbers.
Note: Array should start with a positive number and 0 (zero) should be considered a positive element."""
 
#User function Template for python3
from array import *

class Solution:
    def rearrange(self,arr, n):
        neg=[]
        pos=[]
        arr1=[]
        for num in arr:
            if num<0:
                neg.append(num)
            else:
                pos.append(num)
        i=0
        j=0
        k=0
        while i<len(pos) and j<len(neg):
            arr[k]=pos[i]
            k+=1
            i+=1
            arr[k]=neg[j]
            k+=1
            j+=1
        while i<len(pos):
            arr[k]=pos[i]
            k+=1
            i+=1
        while j<len(neg):
            arr[k]=neg[j]
            k+=1
            j+=1
            
        return arr  
        # negarr = []
        # posarr = []
        # j = 0
        # l = 0
        # len_array = len(arr)
        
        # for i in range(len_array):
        #     if arr[i] < 0:
        #         negarr.append(arr[i])
        #         j += 1
        #     else:
        #         posarr.append(arr[i])
        #         l += 1
        
        # arr.clear()
        # m = 0
        # n = 0
        # for i in range(len_array):
        #     if i % 2 == 0:
        #         if n < len(posarr):
        #             arr.append(posarr[n])
        #             n += 1
        #     else:
        #         if m < len(negarr):
        #             arr.append(negarr[m])
        #             m += 1
        
        # return arr
        # code here
        # negarr = array('i', [])
        # posarr = array('i', [])
        # j = 0
        # l = 0
        # len_array = len(arr)
        # arr.sort()
        # for i in range(len_array):
        #     if arr[i] < 0:
        #         negarr[j] = arr[i]
        #         j+=1
        #     else:
        #         posarr[l] = arr[i]
        #         l+=1
        
        # arr.empty()
        # m = 0
        # n = 0
        # for i in range(len_array):
        #     if (i%2 == 0):
        #         arr[i] = negarr[m]
        #         m+=1
        #     else:
        #         arr[i] = posarr[n]
        
        
        # return arr[n]
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	tc = int(input())
	while tc > 0:
		n = int(input())
		arr = list(map(int, input().strip().split()))
		ob = Solution()
		ob.rearrange(arr, n)
		for x in arr:
			print(x, end=" ")
		print()
		tc -= 1

# } Driver Code Ends
