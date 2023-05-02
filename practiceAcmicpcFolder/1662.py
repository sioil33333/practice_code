#https://www.acmicpc.net/problem/1662

if __name__ == '__main__':
    s = input()
    
    stack = []
    
    cnt = 0
    bef = ""
    for string in s:
        if string == '(':
            stack.append([cnt-1, bef])
            cnt = 0
        elif string == ')':
            cor = stack.pop()
            cnt = cnt*cor[1] + cor[0]
        else:
            cnt += 1
            bef = int(string)
    print(cnt)
    