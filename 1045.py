

if __name__ == '__main__' :
    n = input() 
    inputs = raw_input()
    _inputs = inputs.split()
    number = 0
    output = []
    i = 0 

    real_inputs = [ int(each) for each in _inputs ]
     
    sort_inputs = sorted(real_inputs)

    while True :
        ob = real_inputs[i] 
        if ob == sort_inputs[i] :
            i += 1
            number += 1
            output.append(ob)
        
        else :
            i = sort_inputs.index(ob) + 1
        if i> n - 1 :
            break
    

    if number == 0 :
        print '0'
        print 
    else :
        print number 
        for i in output :
            print i ,
