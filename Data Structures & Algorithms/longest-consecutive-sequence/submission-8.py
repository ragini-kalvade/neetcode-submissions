class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        nums_len = len(nums)
        seen = set(nums)

        for num in seen:
            
            if num - 1 not in seen:
                current_start = num
                length = 1
                while current_start+1 in seen:
                    length+=1
                    current_start+=1  
        
                longest = max(longest, length)

        return longest


        