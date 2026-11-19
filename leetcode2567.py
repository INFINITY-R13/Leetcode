class Solution:
    def minimizeSum(self, nums: list[int]) -> int:
        nums.sort()
        n = len(nums)
        # Change two smallest → range = nums[n-1] - nums[2]
        # Change one smallest + one largest → range = nums[n-2] - nums[1]
        # Change two largest → range = nums[n-3] - nums[0]
        return min(
            nums[n - 1] - nums[2],
            nums[n - 2] - nums[1],
            nums[n - 3] - nums[0]
        )
