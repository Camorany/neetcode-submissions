class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        countDict = dict()
        minVal, maxVal = min(nums), max(nums)

        for num in nums:
            countDict[num] = countDict.get(num, 0) + 1
        
        print(countDict)
        

        arrayPointer = 0
        for num in range(minVal, maxVal + 1):
            while countDict.get(num, 0) > 0:
                nums[arrayPointer] = num
                arrayPointer += 1
                countDict[num] -= 1
        
        return nums