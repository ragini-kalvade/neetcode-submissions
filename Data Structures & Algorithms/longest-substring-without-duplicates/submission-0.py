class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        slow,fast = 0, 0
        substr_len = 0
        seen = {}

        for fast in range(len(s)):
            seen[s[fast]] = seen.get(s[fast], 0) + 1
            while seen[s[fast]] > 1: 
                seen[s[slow]] -= 1
                slow+=1
            substr_len = max(substr_len,fast - slow + 1)
            
        return substr_len
           
            


        