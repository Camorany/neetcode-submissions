import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestSeq = 0

        for num in nums:
            if (num - 1) not in nums:
                tempSeq = 0
                while (num + tempSeq) in numsSet:
                    tempSeq += 1
                longestSeq = max(longestSeq, tempSeq)    
        
        return longestSeq