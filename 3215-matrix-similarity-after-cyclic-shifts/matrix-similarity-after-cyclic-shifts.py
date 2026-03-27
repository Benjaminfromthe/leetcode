class Solution:
    def areSimilar(self, mat: list[list[int]], k: int) -> bool:
        n = len(mat[0])
        # We only need to check if each row is 'k-periodic'
        # Because shifting left/right by k is functionally the same 
        # check for equality in a cyclic array.
        for row in mat:
            for j in range(n):
                # Check the element k positions away (cyclic)
                if row[j] != row[(j + k) % n]:
                    return False
        return True