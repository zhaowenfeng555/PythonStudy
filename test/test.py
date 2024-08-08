class Solution:
    def isHappy(self, n: int) -> bool:
        dict_visited = {}
        while True:
            if n == 1:
                return True
            output = []
            new_n = 0
            o = 0
            while n > 0:
                output.append(str(n % 10))
                n /= 10
                new_n = (new_n * 10) + (n % 10)
                o += (n % 10) ** 2
            print(output)
            print(new_n)
            output.sort()
            sort_new_n = int(''.join(output))
            if sort_new_n in dict_visited:
                return False
            else:
                dict_visited[sort_new_n] = 1
                n = 0

    def happy_desicion(self, n, dict_visited):
        if n in dict_visited:
            return False
        else:
            output = []
            while n > 0:
                output.append(n % 10)))
                n /= 10
                print(output)
                output.sort()
                new_n = int(''.join(output))

