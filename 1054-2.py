
import string 
nums = string.digits + '-' +'.'

def tell_char(n) :
    tell = 0
    for i in n :
        if i not in nums :
            tell = tell + 1
            return False
    if tell == 0 :
        return True 

def tell_border(n) :
    if '.' in n :
        float_n = float(n)
        if float_n >1000.0 or float_n < -1000.0 :
            return False
        else :
            return True 
    else :
        int_n = int(n)
        if int_n > 1000 or int_n <-1000 :
            return False
        else :
            return True 

def tell_minus(n) :
    if '-' in n :
        char = [i for i in n ]
        if char.count('-') > 1 or char[0] != '-' :
            return False
        else :
            return True
    else :
        return True


def tell_point(n) :
    if '.' in n :
        lens = len(n)
        char = [ i for  i in n ]
        if  char[lens - 1] == '.' :
            return False
        else :
            
            if char.count('.') > 1 :
                return False 
            else :
                if lens <= 2 :
                    return False
                elif lens == 3 and char[1] != '.' and '-' not in n :
                    return False
                elif lens == 3 and '-' in n :
                    return False
                elif lens == 4 and '-' in n and char[2] != '.' :
                    return False 
                elif lens == 4 and '-' not in n and '.' not in char[-3:] :
                    return False
                elif lens > 4 and '.' not in char[-3:]   :
                    return False
                else :
                    return True

    else :
        return True 
            

if __name__ == '__main__':
    n = input()
    inputs = raw_input() 
    number = inputs.split()
    sumall = 0.0
    count = 0 
    for n in number :
        if tell_char(n) == False :
            print ('ERROR: %s is not a legal number' % n )
        else :
            if tell_minus(n) == False :
                print ('ERROR: %s is not a legal number' % n )
            else :
                if tell_point(n) == False :
                    print ('ERROR: %s is not a legal number' % n )
                else :
                    if tell_border(n) == False :
                        print ('ERROR: %s is not a legal number' % n )
                    else :
                        if '.' in n :
                            sumall = sumall + float(n)
                            count = count + 1
                        else :
                            sumall = sumall + int(n)
                            count = count + 1

if count == 0 :
    print ("The average of 0 numbers is Undefined")
else :
    print ('The average of %d numbers is %.2f' % (count ,sumall/count)) 

