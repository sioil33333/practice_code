if __name__ == '__main__':
    for _ in range(int(input())):
        results = 0
        alphabet = [0]*26
        strings = input()
        for string in strings:
            alphabet[ord(string)-65] += 1
        for i in range(len(alphabet)):
            if not alphabet[i]:
                results += 65+i
        print(results)