class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) -1
        max_area = 0

        while l < r:
            width = r - l
            area = min(heights[l],heights[r]) * width
            max_area = max(max_area,area)
            
            if heights[l]>heights[r]:
                r-=1
            else:
                l+=1
        
        return max_area