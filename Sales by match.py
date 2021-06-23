def sockMerchant(n, ar):
    ar.sort()
    count = 0
    i=0
    while i<(len(ar)-1):
        if ar[i]==ar[i+1]:
            count+=1
            i+=2
        else:
            i+=1
            
    return count
            
        
        
#if __name__ == '__main__':
  
n = int(input())
ar = list(map(int, input().split()))
print(sockMerchant(n, ar))

