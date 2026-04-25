class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        def merge(arr, L, M , R):
            leftSubarray = arr[L:M+1]
            rightSubarray = arr[M+1:R+1]

            i, j, k = L, 0, 0

            while j < len(leftSubarray) and k < len(rightSubarray):
                if leftSubarray[j] <= rightSubarray[k]:
                    arr[i] = leftSubarray[j]
                    j +=1
                else:
                    arr[i] = rightSubarray[k]
                    k += 1
                i += 1
            
            while j < len(leftSubarray):
                arr[i] = leftSubarray[j]
                j += 1
                i += 1
            
            while k < len(rightSubarray):
                arr[i] = rightSubarray[k]
                k += 1
                i += 1

        def mergeSort(arr, L, R):
            if L >= R:
                return 
            
            M = (L + R) // 2

            mergeSort(arr, L, M)
            mergeSort(arr, M+1, R)
            merge(arr, L, M, R)

        
        mergeSort(nums, 0, len(nums) - 1)
        return nums
            