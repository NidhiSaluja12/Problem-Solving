def minion_game(string):
    length = len(string)
    vowel, cons = 0, 0

    for i in range(length):
        if string[i] in 'AEIOU':
            vowel = vowel + (length - i)
        else:
            cons = cons + (length - i)

    if vowel > cons:
        print("Kevin", vowel)

    elif vowel < cons:
        print("Stuart", cons)

    else:
        print("Draw")
    # your code goes here


string = input()
print(minion_game(string))
