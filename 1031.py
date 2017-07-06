import string
nums = string.digits
def tell_number(n) :
    for i in n :
        if i not in nums :
            return False

def sum_all(n) :
    s = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    b = [int(i) for i in n ]
    sumall = 0
    for i , j in zip(s,b):
        sumall += i*j
    return  sumall % 11

def tell_legal(a,b) :
    if b == 'X' :
        b = 10
    c = int(b)
    if 2 <= a <= 10 :
        if a + c != 12 :
            return  False
    else :
        if a + c != 1 :
            return False
    return True

if __name__ == '__main__' :
    n = input()
    outputs = []
    for i in range(n) :
        one_id = raw_input()
        if tell_number(one_id[:17])== False :
            outputs.append(one_id)
        elif tell_legal(sum_all(one_id[:17]),one_id[17] ) == False :
            outputs.append(one_id)

    if len(outputs) == 0 :
        print 'All passed'
    else :
        for i in outputs :
            print i
