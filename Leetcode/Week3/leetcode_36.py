# class Solution {  极好的一个C++解法  就是
# public:
#     bool isValidSudoku(vector<vector<char> > &board) {
#         for(int i =    0; i < 9; i ++)
#         {
#             unordered_map<char, bool> m1;   //check i_th row
#             unordered_map<char, bool> m2;   //check i_th column
#             unordered_map<char, bool> m3;   //check i_th subgrid
#             for(int j = 0; j < 9; j ++)
#             {
#                 if(board[i][j] != '.')
#                 {
#                     if(m1[board[i][j]] == true)
#                         return false;
#                     m1[board[i][j]] = true;
#                 }
#                 if(board[j][i] != '.')
#                 {                                   #实际就是把每个九宫格展开为一列来找的规律- -
#                     if(m2[board[j][i]] == true)  # 可见对于每三个九宫格行号增3；对于单个九宫格，每三个格点行号增1。
                                                    #可见对于下个九宫格列号增3，循环周期为3；对于单个九宫格，每个格点行号增1，周期也为3。
#                         return false;
#                     m2[board[j][i]] = true; #分配  一个东西就像字典 加字典东西
#                 }
#                 if(board[i/3*3+j/3][i%3*3+j%3] != '.')            这个是通过找行列的索引规律找出来的
#                 {
#                     if(m3[board[i/3*3+j/3][i%3*3+j%3]] == true)
#                         return false;
#                     m3[board[i/3*3+j/3][i%3*3+j%3]] = true;
#                 }
#             }
#         }
#         return true;
#     }
# };


import collections #初始化字典的功能
class Solution(object):


    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9):
            m1 = collections.defaultdict(bool, m1={})
            m2 = collections.defaultdict(bool, m1={})
            m3 = collections.defaultdict(bool, m1={})
            for j in range(9):
                if board[i][j] != '.':
                    if m1[board[i][j]] == True:
                        return False
                    m1[board[i][j]] = True
                if board[j][i] != '.':
                    if m2[board[j][i]] == True:
                        return False
                    m2[board[j][i]] = True
                if board[(i / 3) * 3 + j / 3][i % 3 * 3 + j % 3] != '.':
                    if m3[board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3]] == True:
                        return False
                    m3[board[i / 3 * 3 + j / 3][i % 3 * 3 + j % 3]] = True
        return True


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        for i in range(9):
            for j in range(9):
                c = board[i][j]
                if c == '.':
                    continue
                if (i, c) in seen or (c, j) in seen or (i/3, j/3, c) in seen:
                    return False
                seen.add((i, c))
                seen.add((c, j))
                seen.add((i/3, j/3, c))  #利用集合来去重- -
        return True


class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        check_set = set()
        for i, row in enumerate(board):
            for j, num in enumerate(row):
                if num != '.':
                    if (i, num) in check_set or (num, j) in check_set or (i/3, j/3, num) in check_set:
                        return False
                    else:
                        check_set.add((i, num))
                        check_set.add((num, j))
                        check_set.add((i/3, j/3, num))
        return True

