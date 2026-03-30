class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        
        def backtrack(i, current_path, current_total):
            # Base Case 1: Success! We found a valid combination
            if current_total == target:
                res.append(list(current_path))
                return
            
            # Base Case 2: Failure! Exceeded target or ran out of candidates
            if i >= len(candidates) or current_total > target:
                return
            
            # Decision 1: Include candidates[i]
            # We add it to our path and KEEP the index at 'i' (allowing reuse)
            current_path.append(candidates[i])
            backtrack(i, current_path, current_total + candidates[i])
            
            # Decision 2: Skip candidates[i] (Backtrack)
            # We remove the element we just added and move to the next index
            current_path.pop()
            backtrack(i + 1, current_path, current_total)
            
        backtrack(0, [], 0)
        return res