class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        left = 0
        right = len(height) - 1

        max_l = height[left]
        max_r = height[right]

        water = 0

        while left < right:
            if max_l < max_r:
                left += 1
                max_l = max(max_l, height[left])
                water += max_l - height[left]
            else:
                right -= 1
                max_r = max(max_r, height[right])
                water += max_r - height[right]

        return water