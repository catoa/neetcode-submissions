class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        def backtrack(s: str, open_parens: int, closed_parens: int):
            if len(s) == 2 * n:
                result.append(s)
                return
            
            if open_parens < n:
                backtrack(s + "(", open_parens + 1, closed_parens)
            if closed_parens < open_parens:
                backtrack(s + ")", open_parens, closed_parens + 1)

        backtrack("", 0, 0)
        return result
        



        
