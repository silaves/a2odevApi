def queensAttack(n, k, rq, cq, obstacles):
    top = n - rq
    right = n - cq
    down = rq - 1
    left = cq - 1

    ext_topright = top if top<right else right
    ext_downright = right if right<down else down
    ext_downleft = left if left<down else down
    ext_topleft = top if top<left else left
    

    for obs in obstacles:
        x = obs[0]
        y = obs[1]

        if y == cq and x > rq:
            c = x-rq-1
            top = c if c<top else top

        elif x > rq and y > cq:
            if abs(x-rq) == abs(y-cq):
                c = x-rq-1
                ext_topright = c if c<ext_topright else ext_topright
            
        elif x == rq and y > cq:
            c = y-cq-1
            right = c if c<right else right

        elif x < rq and y > cq:
            if abs(x-rq) == abs(y-cq):
                c = rq-x-1
                ext_downright = c if c<ext_downright else ext_downright

        elif x < rq and y == cq:
            c = rq-x-1
            down = c if c<down else down

        elif x < rq and y < cq:
            if abs(x-rq) == abs(y-cq):
                c = rq-x-1
                ext_downleft = c if c<ext_downleft else ext_downleft

        elif x == rq and y < cq:
            c = cq-y -1
            left = c if c<left else left

        elif x > rq and y < cq:
            if abs(x-rq) == abs(y-cq):
                c = x-rq-1
                ext_topleft = c if c<ext_topleft else ext_topleft

    return top+right+down+left+ext_topright+ext_downright+ext_downleft+ext_topleft