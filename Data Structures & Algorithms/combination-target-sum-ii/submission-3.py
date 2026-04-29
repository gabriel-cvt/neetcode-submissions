class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def brt(start, path, total):
            if total == target:
                result.append(path[:])
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])
                brt(i + 1, path, total + candidates[i])
                path.pop()

        candidates.sort()
        brt(0, [], 0)
        return result
                