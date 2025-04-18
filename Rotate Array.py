class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n  # To handle cases where k is larger than n
        nums[:] = nums[-k:] + nums[:-k]
