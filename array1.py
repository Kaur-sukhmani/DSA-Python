# Reverse words in a given string

# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        words = S.split('.')
        reverse_string = '.'.join(reversed(words))
        return reverse_string 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends


"""Leetcode """
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        p = ' '.join(s)
        return str(p)



# Reverse words in a given string

# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,S):
        # code here 
        words = S.split('.')
        reverse_string = '.'.join(reversed(words))
        return reverse_string 


#{ 
 # Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        print(obj.reverseWords(s))

# } Driver Code Ends


"""Leetcode """
class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split()
        s = s[::-1]
        p = ' '.join(s)
        return str(p)



