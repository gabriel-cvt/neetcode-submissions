class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        
        array = sorted(nums)

        result = []

        for i in range(n):
            if i > 0 and array[i] == array[i - 1]:
                continue

            l = i + 1
            r = n - 1
            while l < r:
                total = array[i] + array[r] + array[l]
                if total == 0:
                    result.append([array[i], array[l], array[r]])
                    l += 1
                    r -= 1

                    while l < r and array[l] == array[l - 1]:
                        l += 1

                    while l < r and array[r] == array[r + 1]:
                        r -=1
                    
                elif total > 0:
                    r -= 1
                else:
                    l += 1
        return result