
import string 
nums = string.digits + '-' +'.'


def tell_digit(n) :

    real_n = float(n)
    list_n = [ i for i in n]
    lens = len(list_n)
    try :
        index_ = list_n.index('-')
    except:
        index_ = -1
        pass

    try :
        index_1 = list_n.index('.') 
    except :
        index_1 = 0 
        pass 
    if real_n == 0 :
        if '-' in list_n and lens == 2 :
            return True 
        elif '-' not in list_n and lens == 1 :
            return True 
        else :
            return False 
    else :
        if '.' not in list_n :
            if list_n[index_+1] == '0' :
                return False
            else :
                return True 
        else :
            if  -1 < real_n < 1 :
                if  '-' in list_n and  '.' in list_n[1:3] :
                    return True 
                elif '-' not in list_n and '.' in list_n[0:2] :
                    return True 
                else :
                    return False
            else :
                if list_n[index_+1] != '0' and '-' in n :
                    return True 
                elif list_n[index_+1] != '0' and '-' not in n  :
                    return True
                else :
                    return False 


                    


            
                

def tell_char(n) :
    tell = 0
    for i in n :
        if i not in nums :
            tell = tell + 1
            break 
    if tell == 0 :
        return True
    else :
        return False

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
        if char.count('-') > 1 :
            return False
        else :
            if char[0] != '-' :
                return False
            else :
                return True
    else :
        return True


def tell_point(n) :
    if '.' in n :
        lens = len(n)
        char = [ i for  i in n ]
        if char.count('.') >1 :
            return False 
        else :
            index = char.index('.')
            if lens == 1 :
                return False
            if lens == 2 and char[1] != '-' :
                return True
            if lens == 3 :
                if '-' in char :
                    return True
                else :
                    if index == 0 :
                        return False
                    else :
                        return True 
            if lens == 4 :
                if '-' in char :
                    return True
                else :
                    if index == 0 :
                        return False
                    else :
                        return True 
            if lens >= 5 :
                if '.' in char[-3:] :
                    return True
                else :
                    return False

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
            if n == '-.' :
                n = '0'
            else :
                pass
            if tell_minus(n) == False :
                print ('ERROR: %s is not a legal number' % n )
            else :
                if tell_point(n) == False :
                    print ('ERROR: %s is not a legal number' % n )
                else :
                    if tell_border(n) == False :
                        print ('ERROR: %s is not a legal number' % n )
                    else :
                        if tell_digit(n) == False :
                            print ('ERROR: %s is not a legal number' % n)
                        else :
                            sumall = sumall + float(n)
                            count = count + 1
                    

if count == 0 :
    print ("The average of 0 numbers is Undefined" )
elif count == 1 :
    print ("The average of 1 number is %.2f" % (sumall ))
else :
    print ('The average of %d numbers is %.2f' % (count ,sumall/count)) 

