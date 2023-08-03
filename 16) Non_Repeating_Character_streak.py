# User function Template for python3

class Solution:

    # Function to find the first non-repeating character in a string.
    def nonrepeatingcharacter(s):
        # code here
        for idx in s:
            # if idx == ptr:
            #     pass
            # else:
            k = s.index(idx)
            if s.count(idx) == 1:
                return idx

        return -1


# {
# Driver Code Starts
# Initial Template for Python 3

import atexit
import io
import sys

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        s = str(input())
        obj = Solution()
        ans = obj.nonrepeatingcharacter(s)
        if (ans != '$'):
            print(ans)
        else:
            print(-1)

# } Driver Code Ends
