def solve(s):
    s1 = s.split(" ")
    l = []
    for word in s1:
        if word.isdigit() == True:
            l.append(word)
        else:
            l.append(word.capitalize())

    newStr = " ".join(l)
    return newStr


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = raw_input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
