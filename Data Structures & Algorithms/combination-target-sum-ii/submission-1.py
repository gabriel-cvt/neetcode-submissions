class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def brt(start, path):
            if sum(path) == target:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if sum(path) + candidates[i] > target:
                    continue
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                path.append(candidates[i])
                brt(i + 1, path)
                path.pop()
        brt(0, [])
        return result
                