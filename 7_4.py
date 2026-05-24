n = int(input())
def backtrack(remaining, start, path):
    
    if remaining == 0:
        print(*path)
        return
    
    for i in range(start, remaining + 1):
        path.append(i)

        backtrack(remaining - i, i, path)
        path.pop()
backtrack(n, 1, [])