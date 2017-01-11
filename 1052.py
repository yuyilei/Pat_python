

def remove(n) :
    a = [ i for i in n.split('[') ]
    b = ''.join(a)
    c = [ i for i in b.split(']')]
    for  index, i in enumerate(c) :
        if i == '' or i == ' ' :
            del c[index]
        if ' ' in i:
            c[index] = i.split()[0]
    return c



if __name__ == '__main__' :
    hands = input()
    eyes = input()
    mouth = input() 
    real_hands = remove(hands)
    real_eyes = remove(eyes)
    real_mouth = remove(mouth)
    n =  int(input())
    real_res = [] 
    for i in range(n) :
        number = input().split()
        real_n = [ int(i) for i in number ]
        try :
            output = \
            real_hands[real_n[0]-1]+'('+real_eyes[real_n[1]-1]+real_mouth[real_n[2]-1]+real_eyes[real_n[3]-1]+')'+real_hands[real_n[4]-1]
        except IndexError:
            output = 'Are you kidding me? @\/@'
        real_res.append(output) 

    for each in real_res :
        print(each) 
