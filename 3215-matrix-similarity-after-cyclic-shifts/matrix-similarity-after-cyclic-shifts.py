class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        n= len(mat[0])

        for r in range(len(mat)):
            for i in range(n):
                if mat[r][i] != mat[r][(i+k)%n]:
                    return False
        return True

        