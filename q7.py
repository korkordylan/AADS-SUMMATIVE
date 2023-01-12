import random 

def selection_sort(L):
    """ Sort the list L using SelectionSort (by modifying L). """
    size = len(L)
    for i in range(size):
        min_index = i
 
        for j in range(i + 1, size):
            
            if L[j] < L[min_index]:
                min_index = j
         
        (L[i], L[min_index]) = (L[min_index], L[i])
            
    return L




        
def get_pivot(L):
    """ Pick 5 elements from distinct random positions in L, sort
    them by calling selection_sort, and return the middle element.
    L is guaranteed to have at least 11 elements.
    """
    Lzero = []
    
    ri = random.sample(L, 5)
    
    selection_sort(ri)
         
    return ri[2]

    
def three_partition(L, pivot):
    """ Partition L into a list L0 of elements smaller than pivot,
    a list L1 of elements equal to pivot, and a list L2 of elements
    greater than pivot; return a 3-tuple (L0,L1,L2) of these three
    lists.
    """

    
    L0 = []
    L1 = []
    L2 = []
    L3 = []
    for x in L:
        if x == pivot:
            L1.append(x)
        elif x < pivot:
            L0.append(x)
        else:
            L2.append(x)
    # selection_sort(L1)
    # selection_sort(L2)
    # selection_sort(L0)
    

    return L0, L1 , L2
 

def quick_sort(L):
    """ If L has at most 10 elements, sort L by
    calling selection_sort(L), and then return L.
    Otherwise, call get_pivot(L) to get the pivot, then
    call three_partition(L,pivot) to get the three lists,
    then make the required recursive calls and produce the
    final sorted list and return it.
    """

    if len(L) <= 10:
        selection_sort(L)
        return L 
    else:
        L3 = []
        p = get_pivot(L)
        L0, L1, L2 = three_partition(L, p)
        if len(L0) > 1:
            L0 = quick_sort(L0)
        if len(L2) > 1:
            L2 = quick_sort(L2)
    L = L0 + L1 + L2
   
    return L

# Test selection_sort
L = [10,8,4,6,2,1,5,3,9,7]
selection_sort(L)
assert(L == [1,2,3,4,5,6,7,8,9,10])

# Test get_pivot
L = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
pivot = get_pivot(L)
assert(pivot in L and pivot >= 3 and pivot <= 13)

L = [1,2,5,5,5,5,5,5,5,9,10]
pivot = get_pivot(L)
assert(pivot==5)

# Test three_partition
L0,L1,L2 = three_partition([5,4,3,2,1,18,22,34,44,17,58,29,55,88,12,14,15,5,5,5],5)
assert(sorted(L0)==[1,2,3,4] and L1==[5,5,5,5] and sorted(L2)==[12, 14, 15, 17, 18, 22, 29, 34, 44, 55, 58, 88])

#Test quick_sort
L = quick_sort([5,4,3,2,1,18,22,34,44,17,58,29,55,88,12,14,15,5,5,5])
assert(L==[1, 2, 3, 4, 5, 5, 5, 5, 12, 14, 15, 17, 18, 22, 29, 34, 44, 55, 58, 88])
