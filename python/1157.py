string = input().lower()
l = list(set(string))
count = []

for i in l:
    str_count = string.count(i)
    count.append(str_count)

if count.count(max(count)) >= 2:
    print("?")
else:
    print(l[(count.index(max(count)))].upper())