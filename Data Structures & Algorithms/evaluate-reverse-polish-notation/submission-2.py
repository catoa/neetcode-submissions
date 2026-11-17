class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = {'+', '-', '*', '/'}
        stack = [] # => [5]
        for token in tokens:
            if token in operators:
                # perform calculation
                # assert len(stack) == 2
                rhs = int(stack.pop()) # 4
                lhs = int(stack.pop()) # 9
                res = None
                match token:
                    case '+':
                        res = lhs + rhs
                    case '-':
                        res = lhs - rhs
                    case '*': 
                        res = lhs * rhs
                    case '/':
                        res = int(float(lhs) / rhs)
                stack.append(str(res))
            else:
                stack.append(token)
        assert len(stack) == 1
        return int(stack[0]) 
