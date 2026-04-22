class Solution:
    def sortColors(self, nums: List[int]) -> None:

        for i in range(len(nums) - 1):
            for j in range(i, len(nums)):
                if nums[i] > nums[j]:
                    tempI = nums[i]
                    tempJ = nums[j]
                    nums[i] = tempJ
                    nums[j] = tempI

        