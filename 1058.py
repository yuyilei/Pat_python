
def to_find_brackets(n) :
    list_n = [ i for i in n ]
    index = []
    for each in list_n :
        if each == '(' or each == ')' :
            index.append(list_n.index(each))

    return index

if __name__ == '__main__' :
    inputs = raw_input()
    inputs_ = inputs.split()
    number = int(inputs_[0])
    problem = int(inputs_[1])

    answers = []
    students = []

    for i in range(problem) :
        answers.append(raw_input())
    for i in range(number) :
        students.append(raw_input())


     
