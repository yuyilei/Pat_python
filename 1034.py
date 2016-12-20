from fractions import Fraction 

def change(n) :
    fraction = Fraction(n)
    numerator = abs(fraction.numerator)
    denominator = abs(fraction.denominator) 
    
    if numerator <= denominator or ( numerator > denominator and denominator
                == 1 ) :
        res =  fraction  
        if '-' not in n :
            return res 
        else :
            return -res
    else :
        res1 = numerator / denominator 
        res2 = fraction - res1 
        if '-' not in n :
            return (res1,res2)
        else :
            return (-res1,res2)


def tell_improper(n) :
    fraction = Fraction(n) 
    numerator = abs(fraction.numerator)
    denominator = abs(fraction.denominator) 
    if numerator > denominator and denominator != 1 :
        return True
    else :
        return False


def add(n,m) :
    return Fraction(n) + Fraction(m)

def subtraction(n,m) :
    return Fraction(n) - Fraction(m) 

def multi(n.m) :
    return Fraction(n) * Fraction(m)
def division(n,m) :
    if Fraction(m) == 0 :
        return 'Inf'
    else :
        return Fraction(n) / Fraction(m) 

def result(sumall) :
    if sumall >= 0:
        if sumall > 1 :
            numerator = sumall.numerator
            denominator = sumall.denominator
            res1 = numerator / denominator 
            res2 = sumall - res1 
            if res2 == 0 :
                return res1
            else :
                return (res1 ,res2)
        else :
            return sumall 
    else :
        if sumall < -1 :
            numerator = sumall.numerator 
            denominator = sumall.denominator
            res1 = numerator / denominerator 
            res2 = res1 - sumall 
            if res2 == 0 :
                return res1 
            else :
                return (res1,res2)
        else :
            return sumall


if __name__ == '__main__' :
    inputs = raw_input() 
    inputs_ = inputs.split()
    former = inputs_[0]
    later = inputs_[1] 
    

