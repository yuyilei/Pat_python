
a = raw_input() 
s = a.split() 
number = int(s[0])
space = int(s[1])
first = int(s[2])

users = []

for i in range(0,number) :
    s  =raw_input() 
    users.append(s)

res = [] 

if first > number :
    print "Keep going..."

while first <= number :
    if users[first-1] not in res :
        res.append(users[first-1]) 
        first += space 
    else :
        first += 1 

for each in res :
    print each 

