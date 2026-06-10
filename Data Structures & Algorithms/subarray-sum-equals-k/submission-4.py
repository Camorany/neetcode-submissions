class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        totalSubarrays = 0
        currentSum = 0
        prefixSumDict = {0 : 1}

        for num in nums:
            currentSum += num
            diff = currentSum - k

            totalSubarrays += prefixSumDict.get(diff, 0)
            prefixSumDict[currentSum] = prefixSumDict.get(currentSum, 0) + 1

        return totalSubarrays