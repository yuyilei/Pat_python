
def to_remove_brackets(s) :
    s1  = ''.join(''.join(s.split('(')).split(')'))
    s2 = s1.split()
    s3 = ''.join(s2) 
    for i in s3 :
        try :
            if int(i) :
                s3 = s3.replace(i,'') 
        except :
            pass 
    return s3.split()

def handle_answer(n) :
    list_n = [ i for i in n ]
    number = n[:3] 
    real_number = [int(i) for i in number ]
    real_number.append(''.join(list_n[3:]))
    return real_number
    

if __name__ == '__main__' :
    inputs = raw_input()
    inputs_ = inputs.split()
    number = int(inputs_[0])
    problem = int(inputs_[1])

    answer = []
    students = []
    scores = [ 0 for i in range(number)] 
    error = [] 
    max_error = 0 

    for i in range(problem) :
        answer.append(handle_answer(raw_input().split()))
    for i in range(number) :
        students.append(to_remove_brackets(raw_input()))  
    
    for each in answer:
        index = answer.index(each) 
        errors = 0 
        for each_st in students :
            index_st = students.index(each_st)
            if each_st[index] == each[3] :
                scores[index_st] += each[0] 
            else :
                errors += 1
        if errors > max_error :
            error = []
            max_error = errors 
            error.append(index+1) 
        elif errors == max_error :
            error.append(index+1)

    for each in scores :
        print each 
    if max_error == 0 :
        print 'Too simple'
    else :
        for i in range(len(error)) :
            error.insert(0,max_error) 
        for i in error :
            print i , 


        


     
