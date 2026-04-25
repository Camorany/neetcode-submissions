class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []

        def productOfNumsExpectSelf(numIndex):
            product = 1
            for i in range(len(nums)):
                if i != numIndex:
                 product *= nums[i]
                 
            return product

                


        for i in range(len(nums)):
            output.append(productOfNumsExpectSelf(i))

        return output