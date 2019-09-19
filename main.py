def neg(a):
    return (not a)

def land(a, b):
    if a and b:
        return 1
    else:
        return 0

def lor(a, b):
    if a or b:
        return 1
    else: 
        return 0

def cond(a, b):
    if a == 1 and b == 0:
        return 0
    else:
        return 1

truth_values = (0, 1)

def Statements():
    print('p', 'q', 'r', 's', ' ', 'A', 'B')
    for p in truth_values:
        for q in truth_values:
            for r in truth_values:
                for s in truth_values:
                    print(p, q, r, s, ' ', land((cond(land(p, neg(q)), lor(q, r))), s), land(lor(r, s), cond(p, q)))

Statements()
