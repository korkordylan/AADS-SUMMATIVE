def decode(E):
    result = ""
    for item in E:
        char, count = item
        for i in range(count):
            result += char
    return result

def stretches(S):
    stretch = []
    charadd = S[0]
    count = 0
    for char in S:
        if char == charadd :
            count += 1
        else:
            stretch.append(count)
            charadd = char
            count = 1
    stretch.append(count)
    return stretch

def shrivel(S):    
    shrivelresult = []
    charadd = S[0]
    
    for char in S:
        if char != charadd :
            shrivelresult.append(charadd)
            charadd = char 
    shrivelresult.append(charadd)
    return shrivelresult

def encode(D):
    result = []
    sh = shrivel(D)
    st = stretches(D)
    length = len(sh)
    for i in range(0, length):
        resultadd = sh[i], st[i]
        result.append(resultadd)
    return result

assert type(encode('somestring')) == list, 'encode does not return a list'
assert encode('bookkeeper') == [('b', 1), ('o', 2), ('k', 2), ('e', 2), ('p', 1), ('e', 1), ('r', 1)]

assert type(stretches('aabbcca')) == list, 'stretches does not return a list'
assert stretches('aabbcca') == [2, 2, 2, 1]

assert type(shrivel('aabbcca')) == list, 'shrivel does not return a list'
assert shrivel('hyppyttyyh') == ['h', 'y', 'p', 'y', 't', 'y', 'h']

assert type(decode([('a', 2), ('b', 2)])) == str, 'decode does not return a string'
assert decode([('b', 1), ('o', 2), ('k', 2), ('e', 2), ('p', 1), ('e', 1), ('r', 1)]) == 'bookkeeper'

