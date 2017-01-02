 



def check_PAT(n) :
    if 'P' not in n  or 'A' not in n or 'T' not in n :
        return False
    else :
        return True

def check_PAT2(n) :
    flag = 0
    for i in n :
        if i not in 'PAT' :
            flag = 1
            break 
    if flag == 0 :
        return True 
    else :
        return False
def check_number_A(n) :
    lens = len(n)
    index_P = n.index('P')
    index_T = n.index('T')
    s = index_T - index_P
    if s <= 1  :
        return False
    else :
        if index_P == 0 and index_T == lens -1 :
            return True
        elif (lens -1 -index_T ) == index_P * ( s-1):
            return True
        else :
            return False

def check_PT(n) :
    count_P = n.count('P')
    count_T = n.count('T')
    if count_P == 1 and count_T == 1 :
        return True
    else :
        return False

if __name__ == '__main__' :
    n = input()
    res = []
    for i in range(n) :
        inputs = raw_input() 
        if check_PT(inputs) == True and check_number_A(inputs) == True :
            if check_PAT2(inputs) == True and check_PAT(inputs) == True :
                res.append('YES')
            else :
                res.append('NO')
        else :
            res.append("NO")

    for i in res :
        print i 

        



