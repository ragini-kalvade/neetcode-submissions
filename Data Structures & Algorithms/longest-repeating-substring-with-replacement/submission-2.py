class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        counts = {}
        max_freq = 0
        best = 0

        for right in range(len(s)):
            counts[s[right]] = counts.get(s[right], 0) + 1
            max_freq = max(max_freq, counts[s[right]])

            window_size = right - left + 1

            # chars to replace = window size - most frequent char count
            while window_size - max_freq > k:
                counts[s[left]] -= 1
                left += 1
                window_size = right - left + 1

            best = max(best, window_size)

        return best