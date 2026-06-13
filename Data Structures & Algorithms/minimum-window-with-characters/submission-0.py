class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""

        
        need_len = len(t)

        need = {}
        left = 0

        #hashmap of char needed
        for char in t:
            need[char] = need.get(char,0)+1

        #chars in the window
        have = {}
        have_count = 0
        best_len = float("inf")
        best_start = 0
        for right in range(len(s)):
            schar = s[right]
            have[schar] = have.get(schar,0)+1
            #keep track of the characters that match with 
            #t and add count to needed chars length
            if schar in need and have[schar]<=need[schar]: 
                have_count+=1
            while have_count == need_len:
                window_len = right - left + 1
                if window_len < best_len:
                    best_len = window_len
                    best_start = left
                left_char = s[left]
                have[left_char] -= 1

                if left_char in need and have[left_char] < need[left_char]:
                    have_count -= 1

                left += 1
        if best_len == float("inf"):
            return ""

        return s[best_start:best_start + best_len]


            