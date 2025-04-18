from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()  # Step 1: Sort the array
        closest_sum = float('inf')  # Initializes with infinity

        for i in range(len(nums) - 2):  # Step 2: Iterate through the array
            left, right = i + 1, len(nums) - 1

            while left < right:  # Step 3: Two-pointer technique
                current_sum = nums[i] + nums[left] + nums[right]

                # If the current sum is exactly the target, return it
                if current_sum == target:
                    return current_sum

                # Updates closest sum if the current sum is closer to the target
                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                # Move the pointers
                if current_sum < target:
                    left += 1
                else:
                    right -= 1

        return closest_sum  # Returns the closest sum found
