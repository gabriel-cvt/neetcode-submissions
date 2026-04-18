class Solution:
    def isHappy(self, n: int) -> bool:
        sett = set()

        while True:
            nums = str(n).strip()
            nums2 = [int(x) ** 2 for x in nums]
            result = sum(nums2)
            if result == 1:
                return True
            if result in sett:
                return False
            n = result
            sett.add(result)