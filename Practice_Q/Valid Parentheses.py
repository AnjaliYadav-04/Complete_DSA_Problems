class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for ch in s:
            if ch in pairs:
                # Closing bracket
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                # Opening bracket
                stack.append(ch)
        
        return not stack
