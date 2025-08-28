def validParenthesis(s):
    stack = []
    mapping = { '(': ')', '{': '}', '[': ']' }

    for char in s:
        if char in mapping:  # if it's an opening bracket
            stack.append(mapping[char])  # push its corresponding closing bracket
        else:
            if not stack or stack.pop() != char:
                return False

    return not stack

# Test
print(validParenthesis("()[]{}"))  # True
print(validParenthesis("([)]"))    # False
print(validParenthesis("{[]}"))    # True
