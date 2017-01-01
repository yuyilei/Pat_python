
def to_find_weekday(n,m) :
    al = 'ABCDEFG'
    day = { 'A' : 'MON' , 'B' : 'TUE' ,'C' :'WED' ,'D' :'THU','E' : 'FRI' , 'F'
            :'SAT' , 'G' : 'SUN' } 
    for i in n :
        if i in al :
            index = n.index(i) 
            if m[index] == i :
                key = i 
                break
    return day[key] , index 

def to_find_hour(n,m) :
    al_ = '0123456789ABCDEFGHIJKLMN' 
    hour = { '0' : '00' ,'1' :'01' , '2' :'02' , '3' :'03' , '4' : '04' , '5'
            :'05' , '6' : '06' , '7' : '07' , '8' : '08' , '9' :'09' , 'A' :'10'
            , 'B' : '11' , 'C' :'12','D' :'13', 'E' : '14','F' :'15','G'
            :'16','H' :'17','I':'18','J':'19','K':'20','L':'21','M':'22','N':'23'} 
    lens = len(n) 
    index = to_find_weekday(n,m)[1]

    for i in range(index+1,lens) :
        if n[i] in al_ and n[i] == m[i] :
            key = n[i] 
            break 
    return hour[key]

import string 
alphas = string.letters

def to_find_minute(n,m) :
    lens = len(n)
    for i in range(lens) : 
        if n[i] == m[i] and n[i] in alphas :
            index = i 
            break
    return index 


if __name__ == '__main__' :
    one = raw_input()
    two = raw_input()
    three = raw_input()
    four = raw_input()

    day = to_find_weekday(one,two)[0]
    hour = to_find_hour(one,two)
    minute = str(to_find_minute(three,four))
    
    if len(minute) == 1 :
        minute = '0' + minute 

    res  = day + ' ' + hour + ':' + minute

    print res 

