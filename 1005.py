n = input() 
b = raw_input()
k = b.split()
a = [int(i) for i in k]
res = [int(i) for i in k]  
for c in a :
    while c != 1 :
        if c % 2 == 0 :
            c = c / 2
            if c in a :
                res.remove(c)
            else :
                pass
        else :
            c = (3*c+1)/2 
            if c in a :
                res.remove(c) 
            else :
                pass 
res.sort(reverse = True)
for i in res :
    print i,
