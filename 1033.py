
import string
a = ''
a = raw_input('')
b = ''
b = raw_input('')
c = ''

if '+' not in a :
    for eachchar in b :
        if eachchar.upper() in a :
            pass
        else :
            c = c + eachchar

else :
    for eachchar in b : 
        if eachchar.isupper() :
            pass 
        else :
            if eachchar.upper() in a :
                pass 
            else :
                c  = c + eachchar 


print c 
    
    
