#https://www.acmicpc.net/problem/10830

#함수

#return multificatied Matrix by matrix1 * matrix2
def multificateMatrix(matrix1:list, matrix2:list) -> list:
    global n
    return_matrix = []
    for i in range(n):
        return_matrix.append([])
        for j in range(n):
            cnt = 0
            for k in range(n):
                cnt += (matrix1[i][k]*matrix2[k][j])%1000
            return_matrix[i].append(cnt%1000)
    return_matrix
    return return_matrix

def matrixDC(matrix, b):
    if b == 1:
        return matrix
    else:
        t = matrixDC(matrix, b//2)
        if b % 2 == 0:
            return multificateMatrix(t,t)
        else:
            return multificateMatrix(t,multificateMatrix(t,matrix))
#메인
if __name__ == "__main__":
    #행렬의 크기, 제곱 횟수
    n,b = map(int,input().split())
    #operand matrix
    matrix = []
    for i in range(n):
        matrix.append(list(map(int,input().split())))
    
    matrix = matrixDC(matrix, b)

    for i in range(n):
        for j in range(n):
            print(matrix[i][j]%1000,end =" ")
        print()

