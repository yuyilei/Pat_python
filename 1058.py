
def to_remove_brackets(n) :
    list_n = [ i for i in n ]
    res = []
    flag1 = []
    flag2 = [] 
    for i in range(len(n)) : 
        if list_n[i] == '(' :
            flag1.append(i) 
        if list_n[i] == ')' :
            flag2.append(i) 
    for i , j in zip(flag1,flag2) :
        res.append(''.join(list_n[i+2:j]))  
    return res 

def handle_answer(n) :
    list_n = [ i for i in n ]
    number = n[:3] 
    real_number = [int(i) for i in number ]
    res = real_number.append(''.join(list_n[3:]))
    return res
    

if __name__ == '__main__' :
    inputs = raw_input()
    inputs_ = inputs.split()
    number = int(inputs_[0])
    problem = int(inputs_[1])

    answer = []
    students = []
    scores = [ 0 for i in range(number)] 
    error = []

    for i in range(problem) :
        answer.append(handle_answer(raw_input().split()))
    for i in range(number) :
        students.append(to_remove_brackets(raw_input().split())) 

    max_error = 0

    for each in answer :
        index = answer.index(each) 
        errors = 0 
        for each_st in students :
            index_st = students.index(each_st)
            if each_st[index] == each[3] :
                scores[index_st] += each[0] 
            else :
                errors += 1
        if errors >= max_error :
            max_error = errors 
            error.append(index) 

    for each in scores :
        print each 
    if max_error == 0 :
        print 'Too simple'
    else :
        for i in len(error) :
            error.insert(0,max_error) 
        for i in error :
            print i , 


        


     
