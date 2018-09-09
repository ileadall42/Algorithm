class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.val = self.PossibleVals()
        self.Solver()

    def PossibleVals(self):
        a = "123456789"
        d, val = {}, {}
        for i in range(9):
            for j in range(9):
                ele = self.board[i][j]
                if ele != ".":
                    d[("r", i)] = d.get(("r", i), []) + [ele]
                    d[("c", j)] = d.get(("c", j), []) + [ele]
                    d[(i // 3, j // 3)] = d.get((i // 3, j // 3), []) + [ele]
                else:
                    val[(i, j)] = []  #找出没有填的值放入 val  填了的 行、列、九宫格  位置编号及对应的数字记录在d 字典中
        for (i, j) in val.keys():
            inval = d.get(("r", i), []) + d.get(("c", j), []) + d.get((i / 3, j / 3), [])
            val[(i, j)] = [n for n in a if n not in inval]
        return val

    def Solver(self):
        if len(self.val) == 0:
            return True
        kee = min(self.val.keys(), key=lambda x: len(self.val[x]))
        nums = self.val[kee]
        for n in nums:
            update = {kee: self.val[kee]}
            if self.ValidOne(n, kee, update):  # valid choice
                if self.Solver():  # keep solving
                    return True
            self.undo(kee, update)  # invalid choice or didn't solve it => undo
        return False

    def ValidOne(self, n, kee, update):
        self.board[kee[0]][kee[1]] = n
        del self.val[kee]
        i, j = kee
        for ind in self.val.keys():
            if n in self.val[ind]:
                if ind[0] == i or ind[1] == j or (ind[0] / 3, ind[1] / 3) == (i / 3, j / 3):
                    update[ind] = n
                    self.val[ind].remove(n)
                    if len(self.val[ind]) == 0:
                        return False
        return True

    def undo(self, kee, update):
        self.board[kee[0]][kee[1]] = "."
        for k in update:
            if k not in self.val:
                self.val[k] = update[k]
            else:
                self.val[k].append(update[k])
        return None



s=Solution();
board=[list("53..7...."),
       list("6..195..."),
       list(".98....6."),
       list("8...6...3"),
       list("4..8.3..1"),
       list("7...2...6"),
       list(".6....28."),
       list("...419..5"),
       list("....8...9")];
board2=[
list(".....7..9"),
list(".4..812.."),
list("...9...1."),
list("..53...72"),
list("293....5."),
list(".....53.."),
list("8...23..."),
list("7...5..4."),
list("531.7....")];
s.solveSudoku(board);
print(board);
