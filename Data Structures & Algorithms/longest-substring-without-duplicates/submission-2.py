class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        right, left = 0,0 
        max_len = 0
        char_map = {}
        substr_len = 0
        for right in range(len(s)):
            char_map[s[right]] = char_map.get(s[right],0)+1
            substr_len+=1
            while char_map[s[right]]>1:
                char_map[s[left]]-=1
                substr_len-=1
                left+=1
            max_len = max(max_len, substr_len)

        return max_len
