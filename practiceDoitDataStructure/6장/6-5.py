# 셰이커 정렬 알고리즘 구현하기

from typing import MutableSequence

def shaker_sort(a: MutableSequence) -> None:

    ccnt = 0
    scnt = 0
    left = 0
    right = len(a) - 1
    last = right

    while left < right:
        for j in range(right, left, -1):
            ccnt += 1
            if a[j - 1] > a[j]:
                scnt += 1
                a[j - 1],a[j] = a[j], a[j-1]
                last = j
        left = last

        for j in range(left, right):
            ccnt += 1
            if a[j] > a[j+1]:
                scnt += 1
                a[j], a[j+1] = a[j+1], a[j]
                last = j
        right = last

    print(f'비교를 {ccnt}번 했습니다.')
    print(f'교환을 {scnt}번 했습니다.')
    
if __name__ == '__main__':

    print('셰이커 정렬 수행')
    num = int(input('원소 수 입력.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))
    
    shaker_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')