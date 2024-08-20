class Solution:
    def isValid(self, s: str) -> bool:
        try:
            stack = []
            for i in s:
                if i == ')':
                    if stack.pop() != '(':
                        return False
                elif i == '}':
                    if stack.pop() != '{':
                        return False
                elif i == ']':
                    if stack.pop() != '[':
                        return False
                else:
                    stack.append(i)
        except:
            return False
        if len(stack) > 0:
            return False
        return True

