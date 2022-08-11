# auto grade sat tests

def innput(number):
    '''
    number  ->  number of questions 
    return: a list of answers, warning raised if it's not complete
    '''
    answers = []
    i = 0
    while len(answers) != number:
        if i>0:
            print('!WARNING: Not complete! ReType it!')
        answers.clear()
        i =+ 1
        ansinput = input()
        for _ans in ansinput:
            if _ans=='A':
                answers.append('A')
            if _ans=='B':
                answers.append('B')
            if _ans=='C':
                answers.append('C')
            if _ans=='D':
                answers.append('D')
    return answers
#-------------------------------------------- Li
'''    answers = []
    ansinput = input()
    for _ans in ansinput:
        if _ans=='A':
            answers.append('A')
        if _ans=='B':
            answers.append('B')
        if _ans=='C':
            answers.append('C')
        if _ans=='D':
            answers.append('D')
    try:
        assert len(answers) == number
    except AssertionError:
        print('!WARNING: Not complete! ReType it!')
        answers.clear()'''
#----------------------------------------------
    

def grade(s, solutions, answers):
    '''
    s  ->  amount of questions
    return: incorrects
    '''
    counter = 0
    incor = ''
    if len(answers) != s:
        print('!WARNING: Answers not complete!')
    if len(solutions) != s:
        print('!WARNING: Solutions not complete!')
    for i, _solution in enumerate(solutions):
        if _solution != answers[i]:
            incor = incor + str(i+1) + '. ' + str(_solution) + '\n' 
            #print(i+1,'. ', _solution)
            counter += 1
    return counter, incor
    
def SATgrading():
    '''
    output incorrect questions with solutions and grades
    '''
    s = [52, 44, 15, 30]  # number of questions in each section
    print('input s1 solutions:')
    s1 = innput(s[0])
    print('input s2 solutions:')
    s2 = innput(s[1])
    print('input s3 solutions:')
    s3 = innput(s[2])
    print('input s4 solutions:')
    s4 = innput(s[3])
    
    print('input s1 answers:')
    a1 = innput(s[0])
    print('input s2 answers:')
    a2 = innput(s[1])
    print('input s3 answers:')
    a3 = innput(s[2])
    print('input s4 answers:')
    a4 = innput(s[3])
    
    _score, _incor = grade(s[0],s1,a1)
    print('Section 1: '+str(_score))
    print(_incor)

    _score, _incor = grade(s[1],s2,a2)
    print('Section 2: '+str(_score))
    print(_incor)
    
    _score, _incor = grade(s[2],s3,a3)
    print('Section 3: '+str(_score))
    print(_incor)
    
    _score, _incor = grade(s[3],s4,a4)
    print('Section 4: '+str(_score))
    print(_incor)
    
    return ''

SATgrading()
