class Solution:
    def isValid(self, s: str) -> bool:
        parens_map = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        stack = [] # ["(", "["]
        # "( [ { } ] )"

        for c in s:
            if c in parens_map:
                if stack and stack[-1] == parens_map[c]:
                    stack.pop() # last_paren = "{", c = "}"
                else:
                    return False
            else:
                stack.append(c)

        if stack:
            return False
        else:
            return True
        