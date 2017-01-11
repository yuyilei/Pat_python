

def remove(n) :
    a = [ i for i in n.split('[') ]
    b = ''.join(a)
    c = [ i for i in b.split(']')]
    for index, i in enumerate(c) :
        if i == '' or i == ' ' :
            del c[index]
        if ' ' in i:
            c[index] = i.split()[0]
    return c



if __name__ == '__main__' :
    hands = raw_input()
    eyes = raw_input()
    mouth = raw_input() 
    real_hands = remove(hands)
    real_eyes = remove(eyes)
    real_mouth = remove(mouth)
    len_h = len(real_hands) 
    len_e = len(real_eyes)
    len_m = len(real_mouth)
    n =  int(input())
    real_res = [] 
    for i in range(n) :
        number = raw_input().split()
        real_n = [ int(i) for i in number ]
        if 1<=real_n[0]<=len_h and 1<=real_n[1]<=len_e and 1<=real_n[2]<=len_m and \
                1<=real_n[3]<=len_e and 1<=real_n[4]<=len_h :
            output = \
            real_hands[real_n[0]-1]+'('+real_eyes[real_n[1]-1]+real_mouth[real_n[2]-1]+real_eyes[real_n[3]-1]+')'+real_hands[real_n[4]-1]
        else :
            output = 'Are you kidding me? @\/@'
        real_res.append(output) 

    for each in real_res :
        print(each) 
