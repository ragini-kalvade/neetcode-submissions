class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = 0 
        fast = slow + 1
        length = len(nums)-1
        while slow < length:
            fast = slow+1
            if nums[slow]==0:
                while nums[fast]==0 and fast<length:
                    fast+=1
                temp = nums[fast]
                nums[fast] = nums[slow]
                nums[slow] = temp
            slow+=1
        