class Solution:
    def isValid(self, s: str) -> bool:
        arr = []
        for char in s:
            if char in ['{', '[', '(']: 
                arr.append(char)
            elif char == '}' and len(arr) > 0 and arr[-1] == '{':
                arr.pop()
            elif char == ')' and len(arr) > 0 and arr[-1] == '(':
                arr.pop()
            elif char == ']' and len(arr) > 0 and arr[-1] == '[':
                arr.pop()
            else:
                return False
        return len(arr) == 0