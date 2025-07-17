if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    arr= list(arr)
    # print(arr)
    arr.sort(reverse=True)
    # print ( arr[1] )
    
    for a in arr:
        if a != arr[0]:
            print(a)
            break
