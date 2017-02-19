
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

def Merge(b,low,mid,high) :
    a = [int(i) for i in b]
    i = low 
    j = mid
    t = []
    while(i < mid and j < high) :
        if a[i] <= a[j] :
            t.append(a[i])
            i = i + 1 
        else :
            t.append(a[j])
            j = j + 1 
    if  i < mid :
        t = t + a[i+1:mid]

    if  j < high :
        t = t + a[j+1:high]

    return t 

def merge(N,a,b) :
    real = [int(i) for i in a ]
    relative = [int(i) for i in b ]
    k = 1 
    i = 0 
    c = real
    isMerge = False

    while True :
        if k >= N :
            break 
        while True :
            if i >= N :
                break 
            if i + k*2 <= N :
                c = Merge(c,i,i+k,i+2*k) 
            elif i + k <= N :
                c = Merge(c,i,i+k,N)
            i = i + k * 2

        if ( isMerge ) :
            print "Merge Sort"
            print c 
        elif (c == relative) :
            isMerge = True
            
        k = k * 2

    


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
        merge(N,real,relative) 


        
    
