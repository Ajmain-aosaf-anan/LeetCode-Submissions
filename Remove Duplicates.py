from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        write = 0
        count = 1  # Counts the occurrences of each element

        for read in range(1, len(nums)):
            if nums[read] == nums[read - 1]:
                count += 1
            else:
                count = 1

            if count <= 2:
                write += 1
                nums[write] = nums[read]

        return write + 1
