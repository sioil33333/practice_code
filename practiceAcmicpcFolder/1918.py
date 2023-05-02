#https://www.acmicpc.net/problem/1918

#main
if __name__ == "__main__":
    strings = input()
    checksStack = []
    results = ""
    
    for string in strings:
        if string in ['*', '/']:
            if checksStack:
                if checksStack[-1] in ['*','/']:
                    results += checksStack.pop()
            checksStack.append(string)
        elif string in ["+","-"]:    
            if checksStack:
                if checksStack[-1] in ["+","-"]:
                    results += checksStack.pop()
                elif checksStack[-1] in ['*','/']:
                    while checksStack:
                        if checksStack[-1] != '(':
                            results += checksStack.pop()
                        else:
                            break
            checksStack.append(string)

        elif string == '(':
            checksStack.append('(')
        elif string == ')':
            while checksStack:
                plus = checksStack.pop()
                if plus == '(':
                    break
                results += plus
        else: # 문자일때
            results += string
    while checksStack: results += checksStack.pop()
    print(results)