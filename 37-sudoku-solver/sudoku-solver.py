class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows=[set() for _ in range(9)]
        cols=[set() for _ in range(9)]
        boxes=[set() for _ in range(9)]
        empty_space=[]

        for r in range(9):
            for c in range(9):
                val=board[r][c]
                box_idx=(r//3)*3 +(c//3)
                if val != ".":
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)
                else:
                    empty_space.append((r,c))

        def sudoku(idx):
            if idx >= len(empty_space):
                return True
            r,c = empty_space[idx]
            box_idx=(r//3)*3 +(c//3)
            for i in "123456789":
                if i not in rows[r] and i not in cols[c] and i not in boxes[box_idx]:
                    board[r][c]=i
                    rows[r].add(i)
                    cols[c].add(i)
                    boxes[box_idx].add(i)
                    if sudoku(idx+1):
                        return True
                    board[r][c] ="."
                    rows[r].remove(i)
                    cols[c].remove(i)
                    boxes[box_idx].remove(i)
            return False
        sudoku(0)

