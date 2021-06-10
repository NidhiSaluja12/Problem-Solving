def reverseArray(a):
    revArr = []
    for i in range(arr_count-1, -1, -1):   
        revArr.append(arr[i])
        
    return revArr
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    res = reverseArray(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()

