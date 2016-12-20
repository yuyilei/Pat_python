




if __name__ == '__main__' :
    n = input()
    all_student = []
    for i in range(n) :
        inputs = raw_input()
        inputs_ = inputs.split() 
        all_student.append(inputs_) 
    max_ = int(all_student[0][2]) 
    min_ = int(all_student[0][2])
    index_max = 0 
    index_min = 0
    for each in all_student :
        if max_ < int(each[2]) :
            max_ = int(each[2]) 
            index_max = all_student.index(each)
        if min_ > int(each[2]) :
            min_ = int(each[2]) 
            index_min = all_student.index(each)
    
    print all_student[index_max][0] ,all_student[index_max][1] 
    print all_student[index_min][0] ,all_student[index_min][1]
    

