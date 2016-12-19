

def change_to_decimal(n) :
    number = [ i for  i in  n ]
    mark = number.index('/')
    son_ = ''.join(number[:mark])
    mother_ = ''.join(number[mark+1:])
    mother = float(mother_)
    son = float(son_)
    res  = son / mother 
    return res 

def factor(n) :
    res = [] 
    for each in range(2,n+1) :
        if n % each == 0 :
            res.append(each) 
    return res


if __name__ == '__main__' :
    inputs = raw_input() 
    inputs_list = inputs.split()
    former = change_to_decimal(inputs_list[0]) 
    later = change_to_decimal(inputs_list[1]) 
    mother = int(inputs_list[2])
    res = []
    max_n = int(mother*later)
    min_n = int(mother*former)
    
    for each in range(min_n+1,max_n+1) :
        if mother != each :
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
    
