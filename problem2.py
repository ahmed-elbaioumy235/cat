if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort(reverse = True)
    
    for num in arr[1:] :
    
        if arr[0] != num:
            print(num)
            break
