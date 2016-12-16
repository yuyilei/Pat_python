
import string

nums = string.digits + '.' + '-'
n = input() 
b = raw_input() 
i = 0 
c = b.split()

sumall = 0 
count =  0 
for each in c : 
    for eachchar in each :
        if eachchar not in nums :
        print  'ERROR:',each ,'is not a legal number'
        each = ' '
        else :
            pass 
    if each != ' ' and '.' in each :
        count1 = 0 
        for k in each :
            if k == '.' :
                count1 = count1 + 1
            else  :
                pass 
            if count1 > 1 :
                print  'ERROR:',each,'is not a legal number'
            else :
                if '.' not in each[-3:] and len(each) > 3 :
                    print 'ERROR:',each,'is not a legal number'
                elif each[0] == '.' and len(each) == 3 :
                    print 'ERROR:',each,'is not a legal number'
                else :
                    eachfloat = float(each) 
                    if eachfloat > 1000.0 or eachfloat < -1000.0 :
                        print 'ERROR:',each,'is not a legal number'
                    else:
                        sumall = sumall + eachfloat 
                        count = count + 1
    elif each != ' ' and '.' not in each :
        eachfloat = float(each) 
        if eachfloat > 1000.0 or eachfloat < -1000.0 :
            print 'ERROR:',each,'is not a legal number'
        else :
            sumall = sumall + eachfloat 
            count = count + 1

if count == 0:
    print 'The average of 1 number is Undefined'
else :
    res = round(sumall/count,2)
    print 'The average of',count, 'number is ', res

    
