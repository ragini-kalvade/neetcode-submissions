class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums = sorted(nums)
        results = []
        i = 0
        while i < len(nums)-2:
            left = i+1
            right = len(nums)-1
            while left<right:
                if nums[left]+ nums[right] == -nums[i]:
                    if sorted([nums[left],nums[right],nums[i]]) not in results:
                        results.append(sorted([nums[left],nums[right],nums[i]]))
                    left+=1
                elif nums[left]+ nums[right] > -nums[i]:
                    right-=1
                else:
                    left+=1
            i+=1
        
        return list(results)
        
                
                
        