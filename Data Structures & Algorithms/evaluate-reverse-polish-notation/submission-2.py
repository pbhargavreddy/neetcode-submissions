import math
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        def isNum(val):
            try:
                float(val)
                return True
            except:
                return False
        for i in range(len(tokens)):
            if isNum(tokens[i]):
                stack.append(int(tokens[i]))
            elif tokens[i] == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif tokens[i] == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif tokens[i] == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif tokens[i] == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        return stack.pop()