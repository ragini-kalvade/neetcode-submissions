class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1
        water = 0 
        max_l = height[0]
        max_r = height[right]
        while left < right:
            if max_l < max_r:
                left+=1
                max_l = max(height[left],max_l)
                water+= max_l - height[left]
                
            else:
                right-=1
                max_r = max(height[right],max_r)
                water+=max_r - height[right]
                
        return water

