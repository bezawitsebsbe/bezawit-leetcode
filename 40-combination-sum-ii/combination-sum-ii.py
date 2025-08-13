class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                result.append(path)
                return
            if remaining < 0:
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                backtrack(i + 1, path + [candidates[i]], remaining - candidates[i])

        candidates.sort()  # Sort to facilitate skipping duplicates
        result = []
        backtrack(0, [], target)
        return result
        