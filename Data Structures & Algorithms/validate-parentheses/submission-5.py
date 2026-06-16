class Solution:
    def isValid(self, s: str) -> bool:
        charmap = {
            '(':')',
            '[':']',
            '{':'}'
        }

        stack = []
        for char in s:
            if char in charmap:
                stack.append(char)
            else:
                if not stack:
                    return False
                last_char = stack.pop()
                if charmap[last_char] == char:
                    continue
                else:
                    return False
        if not stack:
            return True 

        return False