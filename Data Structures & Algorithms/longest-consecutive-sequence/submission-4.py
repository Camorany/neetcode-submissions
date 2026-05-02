import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        heapq.heapify(nums)

        print(nums)

        longestCount = 1
        tempCount = 1

        tempVal = heapq.heappop(nums)
        print(tempVal)

        while nums:
            val = heapq.heappop(nums)
            print(val)
            if val == tempVal:
                continue
            if val == tempVal + 1:
                tempCount += 1
            else:
                longestCount = max(longestCount, tempCount)
                tempCount = 1
            tempVal = val

        return max(longestCount, tempCount)