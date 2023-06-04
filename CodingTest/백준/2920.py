num = list(map(int, input().split()))
sortNum = sorted(num)
reverseNum = sorted(num, reverse=True)

if(num == sortNum):
    print("ascending")

elif (num == reverseNum):
    print("descending")
else:
    print("mixed")