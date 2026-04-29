class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""

        for s in strs:
            result += str(len(s)) + "£" + s
        
        return result

    def decode(self, s: str) -> List[str]:
        output = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "£":
                j += 1
            
            stringLength = int(s[i:j])
            stringContent = s[j + 1 : j + 1 + stringLength]
            output.append(stringContent)
            i = j + 1 + stringLength
        
        return output