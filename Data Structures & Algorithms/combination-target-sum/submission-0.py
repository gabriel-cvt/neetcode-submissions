class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path):
            if sum(path) == target:
                result.append(path[:])
                return
            
            for i in range(start, len(nums)):
                if sum(path) + nums[i] > target:
                    continue
                path.append(nums[i])
                backtrack(i, path)
                path.pop()

        backtrack(0, [])
        return result
                