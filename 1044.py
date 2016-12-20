bdict1 = { 0 :'tret' , 1 : 'jan' , 2 : 'feb' , 3 :'mar' , 4 : 'apr', 5:'may' ,6
        : 'jun' ,7 :'jly' , 8: 'aug' ,9 :'sep' ,10 : 'oct' ,11 : 'nov' ,12 :'dec' }

adict1 = { 1 : 'tam' ,2 : 'hel',3 : 'maa' , 4 : 'huh',5 :'tou', 6 :
        'kes',7:'hei', 8 : 'elo' , 9 : 'syy', 10: 'lok',11 : 'mer' ,12 : 'jou' }

bdict2 = { value:key for key,value in bdict1.iteritems() }
adict2 = { value:key for key,value in adict1.iteritems() }

c = ['tam', 'hel', 'maa', 'huh', 'tou', 'kes', 'hei', 'elo', 'syy', 'lok',
        'mer', 'jou']
import string
nums = '1234567890' 

def change_to_Mars(n) :
    a = n / 13
    b = n - a * 13
    if a != 0 :
        if b!= 0 :
            res1 = adict1[a] 
            res2 = bdict1[b]
            return (res1 ,res2) 
        else :
            res1 = adict1[a]
            return (res1,)
    else :
        res = bdict1[b] 
        return (res,)

def change_to_earth(n) :
    number = n.split()
    if len(number) == 1 :
        if number[0] not in c :
            return bdict2[number[0]]
        else :
            return 13*adict2[number[0]]
    else :
        a = adict2[number[0]]
        b = bdict2[number[1]]
        return a*13 + b

if __name__ == '__main__' :
    n = input()
    output = []
    for i  in range(n) :
        inputs = raw_input()
        output.append(inputs)

    for each in output :
        if each[0] in nums :
            int_  = int(each)
            res = change_to_Mars(int_) 
            if len(res) == 1 :
                print  res[0]
            else :
                print res[0],res[1]
        else :
            res  = change_to_earth(each) 
            print res 


    
