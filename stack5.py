"""Reverse a string using Stack
"""
"""You are given a string S, the task is to reverse the string using stack.
Example
1:
Input: S = "GeeksforGeeks"
Output: skeeGrofskeeG
#{"""


# Driver Code Starts

# } Driver Code Ends

def reverse(S):
    list_S = []
    for char in S:
        list_S.append(char)
    list_S.reverse()
    return ''.join(list_S)
    # Add code here


# {
# Driver Code Starts.
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        str1 = input()
        print(reverse(str1))
# } Driver Code Ends
