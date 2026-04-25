class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colourCount = [0] * 3

        for num in nums:
            colourCount[num] += 1
        

        arrayPointer = 0
        for i in range(3):
            while colourCount[i]:
                nums[arrayPointer] = i
                colourCount[i] -= 1
                arrayPointer += 1