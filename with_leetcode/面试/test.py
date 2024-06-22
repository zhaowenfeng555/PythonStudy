# encoding: utf-8
# @author: fengr358
# @time: 2024/6/23 0:21
# @desc:

from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n <= 0:
            return []
        path, result = [], []
        self.backtracking(n, path, result, 0)
        print(result)
        result_output = []
        for item in result:
            item_output = ['.' * n for _ in range(n)]
            for i, j in item:
                item_output[i][j] = 'Q'
            result_output.append(item_output)
        return result_output

    def backtracking(self, n, path, result, startindex):
        if len(path) == n:
            result.append(path[:])
            return
        if len(path) > n:
            return

        for i in range(n):
            for j in range(n):
                if i * n + j < startindex:
                    continue

                flag = True
                for (i_use, j_use) in path:
                    if i == i_use or j == j_use or abs(i - i_use) == abs(j - j_use):
                        flag = False
                        break
                if flag:
                    path.append((i, j))
                    self.backtracking(n, path, result, i * n + j)
                    path.pop()
print(Solution().solveNQueens(4))

