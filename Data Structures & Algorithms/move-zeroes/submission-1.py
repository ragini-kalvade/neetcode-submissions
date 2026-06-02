class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        insert = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[insert], nums[fast] = nums[fast], nums[insert]
                insert += 1
        