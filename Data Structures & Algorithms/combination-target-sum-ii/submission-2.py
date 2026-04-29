class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        path = []
        candidates.sort()

        def brt(start, currSum):
            if currSum == target:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if currSum + candidates[i] > target:
                    continue
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                brt(i + 1, currSum + candidates[i])
                path.pop()
        brt(0, 0)
        return result
                