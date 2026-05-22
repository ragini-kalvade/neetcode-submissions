class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = []

        for i in range(len(nums)):
            if i !=0:
                left.append(left[i-1]*nums[i-1])
            else: 
                left.append(1)
        
        j = len(nums) - 1
        right = [1] * len(nums)
        while j >=0:
            if j!=len(nums)-1:
                right[j] = right[j+1]*nums[j+1]
            else: 
                right[j] = 1 
            j-=1
        result = []   
        for x in range(len(nums)):
            result.append(left[x]*right[x])
        
        return result

                
        
        