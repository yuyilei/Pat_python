def add_to_4(n) :
    if len(n) == 4 :
        res = n
    else :
        res_ = [ i for i in n ]
        for i in range(4-len(n)) :
            res_.append('0')
        res = ''.join(res_) 
    return res

def former_add_to_4(n) :
    if len(n) == 4 :
        res = n
    else :
        a = []
        for i in range( 4 -len(n)) :
            a.append('0')
            _res = ''.join(a)
        res = _res + n 
    return res 

def tell_0(n) :
    if n[0] == n[1] == n[2] == n[3] :
        return False 
    else :
        return True 


def sort_(n) :
    number = [ int(i) for i in n ]
    a = sorted(number)
    b = sorted(number,reverse = True )
    c = [str(i) for  i in a ]
    d = [str(i) for  i in b ]
    former = ''.join(d) 
    later = ''.join(c) 
    return (former , later)

def subtraction(a,b) :
    former = int(a) 
    later = int(b)
    res = former - later 
    res2 = str(res)
    return res2

if __name__ == '__main__' :
    s = raw_input()
    n = add_to_4(s)
    if tell_0(n) == False :
        print ('%s - %s = 0000' % (n,n))
    else :
        while True :
            former , later = sort_(n)
            res = subtraction(former,later)
            print former ,'-',later,'=',former_add_to_4(res)
            if res == '6174' :
                break
            else :
                n = add_to_4(res) 


    
