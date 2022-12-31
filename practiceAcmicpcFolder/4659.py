#비밀번호 발음하기
#https://www.acmicpc.net/problem/4659

aeiou = ['a','e','i','o','u']
while 1:
    strings = input()
    if strings == "end":
        break
    result = 1
    
    #모음 체크
    check = True
    #연속 체크
    checkContinuty = False
    curchr = None
    cnt = 0
    #같은 글자 체크
    checkSame = False

    for i in strings:
        if curchr == i and i not in ['e','o']:
            checkSame = True
            break

        if i in aeiou:
            check = False
            if curchr not in aeiou:
                curchr = i
                cnt = 1
            else:
                cnt += 1
        else:
            if curchr in aeiou or curchr == None:
                curchr = i
                cnt = 1
            else:
                cnt += 1

        if cnt >= 3:
            checkContinuty = True
            break
    if check or checkContinuty or checkSame:
        result = 0
    print("<{0}> is {1}acceptable.".format(strings, "" if result else "not "))