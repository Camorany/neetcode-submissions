class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3

        for num in nums:
            count[num] += 1
        
        arrayIndex = 0
        for i in range(3):
            while count[i]:
                count[i] -= 1
                nums[arrayIndex] = i
                arrayIndex += 1