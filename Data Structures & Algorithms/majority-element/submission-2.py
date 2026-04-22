class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res, count = 0,0

        for number in nums:
            if count == 0:
                res = number

            count += (1 if number == res else -1)
        
        return res