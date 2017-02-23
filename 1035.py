
def tell_insertion(n,a,b) :
    real = [int(i) for i in a ]
    relative = [int(i) for  i in b ]
    flag = 0 
    mark = 0
    for i in range(1,n) :
        each = sorted(real[:n-i]) + real[n-i:]
        if each == relative :
            flag = 1 
            mark = i + 1
            break 
    if flag == 1 :
        return True , mark 
    else :
        return False ,  0 

def merge(real,left,middle,right) : 
    i = left 
    j = middle + 1 
    res = [ i for i in real ] 
    for s  in range(left,right+1) :
        if i > middle :
            res[s] = real[j] 
            j = j + 1 
        elif j > right : 
            res[s] = real[i]
            i = i + 1
        elif real[i] < real[j] :
            res[s] = real[i]
            i = i + 1
        else :
            res[s] = real[j]
            j = j + 1

    return res 


def merge_sort(real,n):
    l = len(real) 
    i = 0
    res = [i for i in real ]
    
    while True : 
        right = min(i+2*n-1,l-1) 
        res = merge(res,i,i+n-1,right) 
        if (i >= l-n):
            break 
        else :
            i=i+2*n 
    return res , 2*n


if __name__ == '__main__' :
    N = input()
    real_ = raw_input()
    relative_ = raw_input()
    real = real_.split()
    relative = relative_.split()
    a,b = tell_insertion(N,real,relative)
    if a == True :
        output = sorted(real[:b+1]) + real[b+1:]
        print 'Insertion Sort'
        for each in output :
            print each ,

    else :
        n = 1
        c = [int(i) for i in real ]
        d = [int(i) for i in relative ]
        while True :
          c , n = merge_sort(c ,n ) 
          if c == d :
              output , n= merge_sort(c,n) 
              break
        print 'Merge Sort'
        for each in output :
            print each , 


        
    
