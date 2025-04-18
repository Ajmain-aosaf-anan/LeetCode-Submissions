from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            # Calculates the width and the height of the container
            width = right - left
            container_height = min(height[left], height[right])

            # Calculates the current area
            current_area = width * container_height
            max_area = max(max_area, current_area)

            # Moves the pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
