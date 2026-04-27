class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = {}
        numFrequency = [[] for _ in range(len(nums) + 1)]

        for num in nums:
            numCount[num] = 1 + numCount.get(num, 0)
        

        for num, nCount in numCount.items():
            numFrequency[nCount].append(num)
        
        output = []
        
        for i in range(len(numFrequency) - 1, 0, -1):
            for value in numFrequency[i]:
                output.append(value)
                if len(output) == k:
                    return output
