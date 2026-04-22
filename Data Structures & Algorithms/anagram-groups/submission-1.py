class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        anagramDict = {} # Key = sortedString, Value = OutputIndex

        for string in strs:
            sortedString = "".join(sorted(string))
            if sortedString in anagramDict:
                output[anagramDict.get(sortedString)].append(string)
            else:
                output.append([string])
                anagramDict[sortedString] = len(output) - 1



        return output 