n = input() 
b = []
c = []
for i in  range(n) :
    a = raw_input()
    a.split()
    b.append(int(a[0:5]))
    b.append(int(a[5:11]))

count = 0
j = []
m = input()
q = []
k = raw_input()
p = k.split()
for i in p:
    q.append(int(i))

for i in q :
    if i not in b :
        c.append(i)
    else :
        j.append(i)

l = len(j) 
for i in range(l) :
    s = b.index(j[i]) 
    if s % 2 == 0 :
        if b[s+1] in j :
            pass 
        else :
            c.append(j[i])
    else :
        if b[s-1] in j :
            pass
        else :
            c.append(j[i])

c.sort()

print len(c)
for i in range(len(c)) :
    print '%d' % c[i] ,



    

