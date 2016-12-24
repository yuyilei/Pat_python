

def change_to_decimal(n) :
    number = [ i for  i in  n ]
    mark = number.index('/')
    son_ = ''.join(number[:mark])
    mother_ = ''.join(number[mark+1:])
    mother = int(mother_)
    son = float(son_)
    res  = son / mother 
    return res 

def factor(n) :
    res = [] 
    for each in range(2,n+1) :
        if n % each == 0 :
            res.append(each) 
    return res

def to_find_mother(n) :
    list_n = [ i for i in n ]
    mark = list_n.index('/')
    mother = ''.join(list_n[mark+1:])
    res = int(mother)
    return res
    


if __name__ == '__main__' :
    inputs = raw_input() 
    inputs_list = inputs.split()
    former = change_to_decimal(inputs_list[0]) 
    later = change_to_decimal(inputs_list[1]) 
    mother = int(inputs_list[2])
    res = [] 
    denominator = to_find_mother(inputs_list[1])
    if mother != denominator and mother != 1 :
        max_n = max(int(mother*later) ,int(mother*former) )
    else :
        max_n = max(int(mother*later),int(mother*former)) -1 
    min_n = min(int(mother*former),int(mother*later)) 
    
    for each in range(min_n+1,max_n+1) :
        if True :
            flag = 0 
            mother_factor = factor(mother) 
            each_factor = factor(each) 
            for i in mother_factor :
                if i in each_factor :
                    flag += 1
                    break 
            if flag == 0 :
                res.append(each) 
    for each in res :
        print '%d/%d' % (each,mother) ,
    
