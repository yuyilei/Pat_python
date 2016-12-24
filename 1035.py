
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

def merge(n,a,b) :
    real = [int(i) for i in a ]
    relative = [int(i) for i in b ]
    for i in range(0,n) :
        if relative[i] <= relative[i+1] :
            pass
        else :
            relative[i+1],relative[i] = relative[i],relative[i+1]
            break 
    return relative 

if __name__ == '__main__' :
    n = input()
    real_ = raw_input()
    relative_ = raw_input()
    real = real_.split()
    relative = relative_.split()
    a,b = tell_insertion(n,real,relative)
    if a == True :
        output = sorted(real[:b+1]) + real[b+1:]
        print 'Insertion Sort'
        for each in output :
            print each ,
    else : 
        print 'Merge Sort'
        output = merge(n,real,relative)  
        for each in output :
            print each ,



        
    
