class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                # Include the candidate number and move to the next
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        candidates.sort()  # Sort candidates to facilitate skipping duplicates
        result = []
        backtrack(0, [], target)
        return result  # Ensure this return is at the correct indentation level

        