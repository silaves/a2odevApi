from .utils.paper_league import solve
from .utils.chess import queensAttack
from .utils.string_value import solve_string

class Problems:

    def problemA(data):
        solution = solve(data)
        return solution

    def problemB(data):
        arr_lines = data.splitlines()
        sp = arr_lines[0].split(' ')
        n = int(sp[0])
        k = int(sp[1])
        sp = arr_lines[1].split(' ')
        rq = int(sp[0])
        cq = int(sp[1])
        obstacles = [[0]*2 for j in range(k)]
        i = 0
        for line in range(2,len(arr_lines)):
            sp = arr_lines[line].split(' ')
            obstacles[i][0] = int(sp[0])
            obstacles[i][1] = int(sp[1])
            i += 1
        solution = queensAttack(n,k,rq,cq,obstacles)
        return solution

    def problemC(data):
        solution = solve_string(data)
        return solution