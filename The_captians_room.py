K = int(input())
array1 = list(map(int, input().split()))
#No_of_groups = len(array1)//K
set1 = set()
set2 = set()

for i in array1:
    if i in set1:
        set2.add(i)
    else:
        set1.add(i)
set3 = set1.difference(set2)
result = list(set3)
print(result[0])
