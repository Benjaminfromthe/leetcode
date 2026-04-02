class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        res = []
        
        def backtrack(start, path):
            # Base case: if the combination is done
            if len(path) == k:
                res.append(list(path))
                return
            
            # Optimization: only iterate through remaining numbers that 
            # can actually finish a combination of length k
            # (n - i + 1) is the number of elements available
            # (k - len(path)) is the number of elements needed
            for i in range(start, n + 1):
                # Add candidate
                path.append(i)
                # Move to next number
                backtrack(i + 1, path)
                # Backtrack: remove candidate to try the next one
                path.pop()
                
        backtrack(1, [])
        return res