from fractions import Fraction 

def change(n) :
    fraction = Fraction(n) 
    numerator = abs(fraction.numerator) 
    denominator = abs(fraction.denominator)
    if numerator != 0 :
        if denominator == 1 :
            res = str(numerator) 
        elif numerator > denominator and denominator != 1 :
            a = numerator / denominator 
            b = numerator % denominator 
            res = str(a) +' ' + str(b)+'/'+str(denominator)
        elif numerator < denominator  :
            res = str(abs(fraction)) 
    if '-' in n and numerator != 0 :
        res_ = '('+'-'+res+ ')'
    elif  numerator == 0 :
        res_ = '0'
    else :
        res_ = res 
    return  res_  

def add_2(a,b) :
    res_ = Fraction(a) + Fraction(b) 
    res = change(str(res_)) 
    return res 

def subtraction_2(a,b) :
    res_ = Fraction(a) - Fraction(b)
    res = change(str(res_)) 
    return res 

def multi_2(a,b) :
    res_ = Fraction(a) * Fraction(b)
    res = change(str(res_))
    return res 

def divsion_2(a,b) :
    if '0' in b :
        res = 'Inf' 
    else :
        res_ = Fraction(a) / Fraction(b) 
        res = change(str(res_))
    return res 

if __name__ == '__main__' :
    inputs = raw_input()
    inputs_ = inputs.split()
    former = inputs_[0]
    later = inputs_[1]
    real_former = change(former) 
    real_later = change(later) 
    print real_former,'+',real_later,'=',add_2(former,later) 
    print real_former,'-',real_later,'=',subtraction_2(former,later)
    print real_former,'*',real_later,'=',multi_2(former,later)
    print real_former,'/',real_later,'=',divsion_2(former,later) 

    
    
