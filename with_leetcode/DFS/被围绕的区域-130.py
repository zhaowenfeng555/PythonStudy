# encoding: utf-8
# @author: fengr358
# @time: 2024/6/17 0:59
# @desc:
#
# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' 组成，捕获 所有 被围绕的区域：
#
# 连接：一个单元格与水平或垂直方向上相邻的单元格连接。
# 区域：连接所有 '0' 的单元格来形成一个区域。
# 围绕：如果您可以用 'X' 单元格 连接这个区域，并且区域中没有任何单元格位于 board 边缘，则该区域被 'X' 单元格围绕。


class Solution:
    def solve(self, board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return board
        map_board = [[0] * len(board[0]) for _ in range(len(board))]
        for i, list_r in enumerate(board):
            for j, item in enumerate(list_r):
                if (i == 0 or j == 0 or i == len(board) - 1 or j == len(board[0]) - 1) and board[i][j] == 'O':
                    stack = [(i, j)]
                    while stack:
                        cur_i, cur_j = stack.pop()
                        if cur_i < 0 or cur_j < 0 or cur_i >= len(board) or cur_j >= len(board[0]) or board[cur_i][
                            cur_j] == 'X' or map_board[cur_i][cur_j] == 1:
                            continue
                        else:
                            map_board[cur_i][cur_j] = 1

                            for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                                stack.append((cur_i + di, cur_j + dj))
        for i, list_r in enumerate(board):
            for j, item in enumerate(list_r):
                if board[i][j] == 'O' and map_board[i][j] == 0:
                    board[i][j] = 'X'
        return board

board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
board = [["O","O"],["O","O"]]
print(Solution().solve(board))



