class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_array = [0] * 26
        s2_array = [0] * 26
        for c in s1:
            index = ord(c) - ord('a')
            s1_array[index] += 1

        l = 0
        for r in range(len(s2)):
            r_index = ord(s2[r]) - ord('a')
            s2_array[r_index] += 1

            if r - l + 1 > len(s1):
                l_index = ord(s2[l]) - ord('a')
                s2_array[l_index] -= 1
                l += 1
            if s1_array == s2_array:
                return True

        return False

            
            