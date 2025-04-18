from typing import List

class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip = [0] * n
        flips = 0
        flip_effect = 0

        for i in range(n):
            # Removes the effect of the flip that has gone out of the window
            if i >= k:
                flip_effect ^= flip[i - k]

            # Determines the current state of the bit considering flip effects
            if nums[i] == flip_effect:
                # If we are at a zero after accounting for flip effects, we need to flip
                if i + k > n:
                    # Not enough space to perform a k-length flip
                    return -1
                # Performs the flip
                flip[i] = 1
                flip_effect ^= 1
                flips += 1

        return flips
