def linz_ordering_eight():
    #store current result 
    R = []
    # keeps track of successive integers 
    D = set()
    def backtracking(size):
        # check if number of elements in R is 8 
        if len(R) == size:
            return True 
        for i in range(size):
            if i in R:
                continue 
            if len(R) > 0:
                Diff = abs((i-R[-1] ))%size 
                if Diff in D:
                    continue
                D.add(Diff)

            else:
                Diff = None
            R.append(i)
            if backtracking(size):
                return True
            R.pop()
            if len(R) > 0:
                D.remove(Diff)
        

    backtracking(8)
    
    return R

def linz_ordering_k(k):
    R = []
    D = []
    def backtracking_k(size):
        if len(R) == size:
            return True
        
        for i in range(size):
            if i in R:
                continue
            if len(R)>0:
                Diff = abs((R[-1]-i))%size
                
                if Diff in D:
                    continue
                D.append(Diff)
            else:
                Diff = None
            R.append(i)
            if backtracking_k(size):
                return True
            R.pop()
            if len(R) > 0:
                D.pop()
    if backtracking_k(k):
        return R
    else:
        return []

assert type(linz_ordering_eight()) == list, 'linz_ordering_eight does not return list'
assert len(linz_ordering_eight()) == 8, 'linz_ordering_k does not return a list of length 8'


assert type(linz_ordering_k(12)) == list, 'linz_ordering_k does not return list'
assert len(linz_ordering_k(12)) == 12, 'linz_ordering_k does not return a list of length 8'
assert set(linz_ordering_k(12)) == set(range(12)), 'linz_ordering_k does not return a permutation'

# assert type(all_linz_orderings_twelve()) == list, 'all_linz_orderings_twelve does not return list'
# assert len(set([tuple(lo) for lo in all_linz_orderings_twelve()])) >= 1928, 'all_linz_orderings_twelve should have at least 1,928 elements'

