class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ""
        smallestString = min(strs, key=len)
        

        for charI in range(len(smallestString)):
            for i in range(1, len(strs)):
                if strs[i][charI] != smallestString[charI]:
                    return output
            output += smallestString[charI]
        
        return output