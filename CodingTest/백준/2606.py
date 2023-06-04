n = int(input())
s = int(input())

array = [[] for _ in range(n+1)]

for _ in range(s):
    x, y = map(int, input().split())
    array[x].append(y)
    array[y].append(x)
visited = [0] * (n+1)


def dfs(array, v, visited):
    visited[v] = 1
    for i in array[v]:
        if visited[i] == 0:
            dfs(array, i, visited)
    return True


dfs(array, 1, visited)
print((sum(visited)-1))
