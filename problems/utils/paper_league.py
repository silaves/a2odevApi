def max_value(idx, value, maxi):
    if value >= maxi[0]:
        maxi[1] = maxi[0]
        maxi[0] = value
        maxi[2] = idx
    return maxi

def calc_values(idx, add_points, points, maxi, count):
    if idx == None:
        points[ count ] += add_points
        maxi = max_value(count, points[count], maxi)
        count += 1
    else:
        points[ idx ] += add_points
        maxi = max_value(idx, points[idx], maxi)
    
    return (points, maxi, count)

def output_format(teams, _solve, played, maxi):
    count_teams = len(teams)
    total_played = (count_teams*count_teams) - count_teams
    result = total_played - played

    if maxi[0] == maxi[1]:
        _solve += 'EMPATE '+str(result)+'\n'
    else:
        for key, value in teams.items():
            if value == maxi[2]:
                _solve += key+' '+str(result)+'\n'
                break
    return _solve

def solve(_str):
    teams = {}
    es = False
    count = 0
    _solve = ''
    played = 0
    points = [0] * 2000
    maxi = [ 0 , 0, -1]
    if len(_str.splitlines())<3:
        return ''
    for line in _str.splitlines():
        if line == 'FIN':
            _solve = output_format(teams, _solve, played, maxi)
            es = False
            count = 0
            played = 0
            points = [0] * 2000
            maxi = [ 0, 0, -1]
            teams.clear()
        else:
            if es:
                inp = line.split(' ')
                played += 1
                team1 = inp[0]
                point1 = int(inp[1])
                team2 = inp[2]
                point2 = int(inp[3])

                if point1 > point2:
                    # idx1 = teams.add(team1, count)
                    idx1= teams.get(team1)
                    teams[team1] = count if idx1==None else idx1
                    points, maxi, count = calc_values(idx1, 2, points, maxi, count)

                    # idx2 = teams.add(team2, count)
                    idx2 = teams.get(team2)
                    teams[team2] = count if idx2==None else idx2
                    points, maxi, count = calc_values(idx2, 1, points, maxi, count)
                else:
                    # idx2 = teams.add(team2, count)
                    idx2 = teams.get(team2)
                    teams[team2] = count if idx2==None else idx2
                    points, maxi, count = calc_values(idx2, 2, points, maxi, count)

                    # idx1 = teams.add(team1, count)
                    idx1 = teams.get(team1)
                    teams[team1] = count if idx1==None else idx1
                    points, maxi, count = calc_values(idx1, 1, points, maxi, count)
            es = True
    # print(_solve)
    return _solve