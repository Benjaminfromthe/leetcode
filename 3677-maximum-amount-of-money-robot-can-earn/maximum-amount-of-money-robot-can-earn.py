from functools import cache

class Solution:
    def maximumAmount(self, coins: list[list[int]]) -> int:
        m, n = len(coins), len(coins[0])

        @cache
        def dp(r, c, k):
            # Base Case: Reached the start
            if r == 0 and c == 0:
                # If it's a robber and we have neutralizations, we can neutralize it
                if coins[r][c] < 0 and k > 0:
                    return 0
                return coins[r][c]
            
            res = float('-inf')
            
            # Possible previous moves: from above or from the left
            for prev_r, prev_c in [(r - 1, c), (r, c - 1)]:
                if 0 <= prev_r < m and 0 <= prev_c < n:
                    # Option 1: Don't neutralize current cell
                    res = max(res, dp(prev_r, prev_c, k) + coins[r][c])
                    
                    # Option 2: Neutralize current cell (if it's a robber and we have k > 0)
                    if coins[r][c] < 0 and k > 0:
                        res = max(res, dp(prev_r, prev_c, k - 1))
            
            return res

        # We start at the bottom-right and can have 0, 1, or 2 neutralizations left
        return max(dp(m - 1, n - 1, 0), dp(m - 1, n - 1, 1), dp(m - 1, n - 1, 2))