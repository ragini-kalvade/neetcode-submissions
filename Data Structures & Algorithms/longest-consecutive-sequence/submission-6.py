class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        longest = 0
        nums_len = len(nums)
        seen = set(nums)
        i = 0
        current_start = 0
        length = 0 
        while i < nums_len:
            
            if nums[i] - 1 not in seen:
                current_start = nums[i]
                length = 1
            while current_start+1 in seen:
                length+=1
                current_start+=1  
            i+=1
            longest = max(longest, length)

        return longest


        