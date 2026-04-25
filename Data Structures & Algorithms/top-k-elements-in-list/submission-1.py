class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numCount = Counter(nums)

        output = []

        for _ in range(k):
            currentMax = max(numCount, key=numCount.get)
            output.append(currentMax)
            numCount.pop(currentMax)

        return output  