# 단순 선택 정렬 알고리즘 구현하기

from typing import MutableSequence

def selection_sort(a: MutableSequence) -> None:

    n = len(a)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if a[j] < a[min]:
                min = j
        
        a[min], a[i] = a[i], a[min]

if __name__ == '__main__':

    print('선택 정렬 수행')
    num = int(input('원소 수 입력.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    selection_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')