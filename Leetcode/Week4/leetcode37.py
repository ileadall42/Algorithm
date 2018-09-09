# class Solution
# {    #思路就是遇到空格 就填入一个1-9的数字判断是否有效  且继续向下判断  如果有效return true  如果9个数字都填完了都没效就return false
# public:
#     bool isValid(vector<vector<char> > &board, int x, int y)
#     {
#         int i, j;
#         for (i = 0; i < 9; i++)
#             if (i != x && board[i][y] == board[x][y])
#                 return false;
#         for (j = 0; j < 9; j++)
#             if (j != y && board[x][j] == board[x][y])
#                 return false;
#         for (i = 3 * (x / 3); i < 3 * (x / 3 + 1); i++)
#             for (j = 3 * (y / 3); j < 3 * (y / 3 + 1); j++)
#                 if (i != x && j != y && board[i][j] == board[x][y])
#                     return false;
#         return true;
#     }
#     bool solveSudoku(vector<vector<char> > &board)
#     {
#         for (int i = 0; i < 9; ++i)
#             for (int j = 0; j < 9; ++j)
#             {
#                 if ('.' == board[i][j])
#                 {
#                     for (int k = 1; k <= 9; ++k)
#                     {
#                         board[i][j] = '0' + k;
#                         if (isValid(board, i, j) && solveSudoku(board))
#                             return true;
#                         board[i][j] = '.';
#                     }
#                     return false;
#                 }
#             }
#         return true;
#     }
# };


class Solution(object):
    digits = "123456789"

    def isValid(self, r, c, k, board):
        for i in range(9):
            if board[r][i] == k or board[i][c] == k:
                return False
        m = r - r % 3;
        n = c - c % 3;
        for i in range(m, m + 3):
            for j in range(n, n + 3):
                if board[i][j] == k: return False;
        return True;

    def isSolve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for k in self.digits:
                        if self.isValid(i, j, k, board):
                            board[i][j] = k
                            if self.isSolve(board):
                                return True
                            board[i][j] = '.';
                    return False
        return True

    def solveSudoku(self, board):
        self.isSolve(board)

s=Solution();
board=[list("53..7...."),
       list("6..195..."),
       list(".98....6."),
       list("8...6...3"),
       list("4..8.3..1"),
       list("7...2...6"),
       list(".6....28."),
       list("...419..5"),
       list("....8..79")];
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
