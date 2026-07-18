class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 !=0:
            return False
        open_ = ['[','{','(']
        close_ = [']','}',')']

        stack = []
        for i in range(len(s)):
            stack.append(s[i])
            if s[i] in close_:
                if len(stack) == 1:
                    return False
                if close_.index(stack.pop())!= open_.index(stack.pop()):
                    return False
        return True if not stack else False