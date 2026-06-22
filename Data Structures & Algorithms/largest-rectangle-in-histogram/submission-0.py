class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []  # (start_index, height)
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                index, previous_height = stack.pop()
                width = i - index
                max_area = max(max_area, previous_height * width)
                start = index

            stack.append((start, height))

        for index, height in stack:
            width = len(heights) - index
            max_area = max(max_area, height * width)

        return max_area