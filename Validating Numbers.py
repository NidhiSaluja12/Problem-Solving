N = int(input())
for i in range(N):
    number = input()
    if (number.isnumeric() and len(number)==10 and number[0] in ['7','8','9']):
        print("YES")
    else:
        print("NO")

