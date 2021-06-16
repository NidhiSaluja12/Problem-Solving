def Runner_Up(scores):
    score_len = len(scores)
    winner = runner_up = float('-inf')
    
    for i in range (score_len):
        winner = max(winner, scores[i])
    
    for i in range(score_len):
        if scores[i] != winner:
            runner_up = max(runner_up, scores[i])
            
    return runner_up

if __name__ == '__main__':
    n = int(input())
    scores = list(map(int, input().split()))
    result = Runner_Up(scores)
    print(result)
    

