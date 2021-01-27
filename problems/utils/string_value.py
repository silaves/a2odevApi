class sf:
    def __init__(self):
        self.index = 0
        self.rank = [0, 0]

def SA(_str, n):
    # sf = {
    #     index: 0,
    #     rank: [0, 0]
    # }
    suffixes = [ sf() for _ in range(n) ]
    
    for x in range(n):
        suffixes[x].index = x
        suffixes[x].rank[0] = ord(_str[x]) - ord('a')
        suffixes[x].rank[1] = (ord(_str[x+1])-ord('a')) if x+1<n else -1

    suffixes = sorted(
        suffixes, key = lambda p:(
            p.rank[0], p.rank[1]
        )
    )
    idx = [0]*n
    k=4
    while( k < 2*n ):
        rank = 0
        prev_rank = suffixes[0].rank[0]
        suffixes[0].rank[0] = rank
        idx[ suffixes[0].index] = 0

        for x in range(1, n):
            if suffixes[x].rank[0] == prev_rank and suffixes[x].rank[1] == suffixes[x-1].rank[1]:
                prev_rank = suffixes[x].rank[0]
                suffixes[x].rank[0] = rank
            else:
                prev_rank = suffixes[x].rank[0]
                rank += 1
                suffixes[x].rank[0] = rank
            idx[ suffixes[x].index ] = x
        
        for x in range(n):
            next_index = suffixes[x].index + k//2
            suffixes[x].rank[1] = suffixes[ idx[next_index]].rank[0] if next_index<n else -1

        suffixes = sorted(
            suffixes, key = lambda p:(
                p.rank[0], p.rank[1]
            )
        )
        k *= 2
    sa = [0]*n
    for x in range(n):
        sa[x] = suffixes[x].index
    
    return sa


def LCP(_str, sa):
    maxi = len(_str)
    n = len(sa)
    lcp = [0]*n
    inv_sa = [0]*n
    for x in range(n):
        inv_sa[ sa[x] ] = x
    k = 0
    
    for x in range(n):
        if inv_sa[x] == n-1:
            k = 0
            continue
        y = sa[inv_sa[x]+1]
        
        while( x+k < n and y+k < n and _str[x+k]==_str[y+k] ):
            k += 1
        lcp[inv_sa[x]] = k
        maxi = max(lcp[inv_sa[x]]*2,maxi)
        k = k-1 if k>0 else k
    return (lcp, maxi)

def printArray(_array):
    for x in _array:
        print(x)

def solve_string(_str):
    sufixxArray = SA(_str, len(_str))
    lcp, maxi = LCP(_str, sufixxArray)
    print(maxi)
    return maxi
