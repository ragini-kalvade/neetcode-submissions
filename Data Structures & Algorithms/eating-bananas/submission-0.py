class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)

        while left < right:
            k = (left + right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + k - 1) // k  # ceil(pile / k)

            if hours <= h:
                right = k       # valid; try slower
            else:
                left = k + 1    # too slow

        return left