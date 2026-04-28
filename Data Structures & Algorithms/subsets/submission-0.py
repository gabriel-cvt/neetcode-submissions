class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index, path):
            # caso base
            if index == len(nums):
                result.append(path[:])
                return
            
            # Constraints

            # first choice
            path.append(nums[index])
            backtrack(index +1, path)
            # undo choice
            path.pop()

            # second choice
            backtrack(index + 1, path)
        backtrack(0, [])
        return result



          