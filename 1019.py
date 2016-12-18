
def tell_0(n) :
    if n[0] == n[1] == n[2] == n[3] :
        return False 
    else :
        return True 


def sort(n) :
    number = [ i for i in n ]
    a = sorted(number)
    b = sorted(number,reverse = True )
    former = ''.join(b) 
    later = ''.join(a) 
    return (former , later)

def subtraction(a,b) :
    former = int(a) 
    later = int(b)
    res = former - later 
    res2 = str(res)
    return (res,res2)

if __name__ == '__main__' :
    n = raw_input()
    if tell_0(n) == False :
        print ('%s - %s = 0000' % (n,n))
    else :
        while True :
            sort = sort(n)
            subtraction = subtraction(sort[0],sort[1])
            print sort[0],'-',sort[1],'=',subtraction[0]
            if subtraction[1] == '6174' :
                break
            else :
                n = subtraction[1]


    
