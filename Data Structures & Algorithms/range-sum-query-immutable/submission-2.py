class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixArr = [0 for _ in range(len(nums) + 1)]

        prefixTracker = 0
        for i in range(len(nums)):
            prefixTracker += nums[i]
            self.prefixArr[i + 1] = prefixTracker

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixArr[right + 1] - self.prefixArr[left]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)