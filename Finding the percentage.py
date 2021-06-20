def average_scores():
    query_scores = student_marks[query_name]
    summ = sum(query_scores)
    avg = summ/3
        
    return ("{:.2f}".format(avg))
    
        
if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    res = average_scores()
    print(res)    

