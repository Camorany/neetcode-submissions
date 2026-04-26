class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        constTime = len(nums)//3
        numsCount = Counter(nums)

        for num, count in numsCount.items():
            if count > constTime:
                output.append(num)
        
        return output