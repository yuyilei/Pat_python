
import string

nums = string.digits + '.' + '-'
n = raw_input() 
m = int(n)
c = [] 
i = 0 
for i in range(m) :
    a = raw_input()
    c.append(a)

sumall = 0 
count =  0 
for each in c :
    eachchar = str(each)
    try :
        eachint  = int(each)
    except :
        pass 
    if eachchar not in nums :
        print 'ERROR:',eachchar ,'is not a legal number'
    else :
        if '.' in eachchar :
            if '.' not in eachchar[-4:-1] :
                print 'ERROR:',eachchar ,'is not a legal number '
            else  :
                count = count + 1
                sumall = sumall + eachint 

if count == 0:
    print 'The average of 1 number is Undefined'
else :
    count2 = float(count) 
    res = round(sumall/count2 ,2)
    print 'The average of',count, 'number is ', res

    
