if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    i = [c for c in range(x+1)]
    j = [c for c in range(y+1)]
    k = [c for c in range(z+1)]
    
    result = [[ci, cj, ck] for ci in i for cj in j for ck in k if not ci+ck+cj == n]
    print (result)
