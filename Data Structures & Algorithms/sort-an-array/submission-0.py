import heapq
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        heapq.heapify(nums)
        print(nums)

        returnArray = []

        for i in range(len(nums)):
            returnArray.append(heapq.heappop(nums))


        return returnArray