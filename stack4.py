# Check for Balanced Brackets in an expression (well-formedness)
"""
Input:
{([])}
Output:
true
Explanation:
{ ( [ ] ) }. Same colored brackets can form
balanced pairs, with 0 number of
unbalanced bracket.
"""
def areBracketsBalanced(expr):
    stack = []
    for char in expr:
        if char in ["(", "[", "{"]:
            stack.append(char)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == "(":
                if char != ")":
                    return False
            elif current_char == "[":
                if char != "]":
                    return False
            elif current_char == "{":
                if char != "}":
                    return False

    if stack:
        return False
    else:
        return True


# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"

    if areBracketsBalanced(expr):
        print("Balanced")
    else:
        print("Not Balanced")
