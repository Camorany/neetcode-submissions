import heapq
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsHashSet = set(nums)
        longestSeq = 0

        for num in numsHashSet:
            if (num - 1) not in nums:
                tempSeq = 0
                while (num + tempSeq) in numsHashSet:
                    tempSeq += 1
                longestSeq = max(longestSeq, tempSeq)    
        
        return longestSeq