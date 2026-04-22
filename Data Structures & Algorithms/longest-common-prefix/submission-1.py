class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""

        # if len(strs) == 1:
        #     return strs[0]
        

        smallestString = min(strs, key=len)
        

        for charI in range(len(smallestString)):
            for string in strs:
                if string[charI] != smallestString[charI]:
                    return output
            output = output + smallestString[charI]
        
        return output