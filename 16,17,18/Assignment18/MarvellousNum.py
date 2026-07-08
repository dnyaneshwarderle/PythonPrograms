def ChkPrime(No):
    fact = 0
    PrimeLst = list()
    if No == 2:
        return True
    for i in range(2,No):
        if No % i == 0:
            PrimeLst.append(i)
    if len(PrimeLst) == 0:
        return True
    else:
        return False
