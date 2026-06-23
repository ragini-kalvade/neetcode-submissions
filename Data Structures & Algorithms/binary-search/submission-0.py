class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        answer = 0

        while left < right:
            mid = (left + right) // 2
            if nums[mid]<target:
                left = mid + 1
            elif nums[mid]>target:
                right = mid
            else:
                return mid
        return -1
            
                
        

        