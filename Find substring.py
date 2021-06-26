def count_substring(string, sub_string):
    ss_count = 0
    s_len = len(string)
    ss_len = len(sub_string)

    for i in range(s_len - 1):
        if string[i:i+ss_len] == sub_string:
            ss_count += 1

    return ss_count
    

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
