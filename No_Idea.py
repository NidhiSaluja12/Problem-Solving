happiness = 0
n1,n2 = map(int,input().split())
array = list(map(int,input().split()))
A = set(list(map(int,input().split())))
B = set(list(map(int,input().split())))

res = sum((i in A)-(i in B) for i in array)
print(res)

