n = int(input())
reset= []
score = input().split()
l = list(map(int, score))
max_score = max(l)

for i in l:
    calcul = i/max_score*100
    reset.append(calcul)

reset_sum = sum(reset)

result = reset_sum/n

print(result)