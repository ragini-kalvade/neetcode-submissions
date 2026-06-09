class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #avoid unnecessary work
        if len(s1)>len(s2):
            return False
        
        s1_chars = {}

        #freq_map for s1
        for char in s1:
            s1_chars[char] = s1_chars.get(char,0)+1
        
        left = 0
        window_chars = {}
        for right in range(len(s2)):
            window_chars[s2[right]] = window_chars.get(s2[right],0) + 1
            if right - left + 1 > len(s1):
                char = s2[left]
                window_chars[char]-=1
                
                if window_chars[char] == 0:
                    del window_chars[char]
                
                left+=1

            if window_chars == s1_chars:
                return True 
            
        return False