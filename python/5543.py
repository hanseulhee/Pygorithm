b = []
d = []

for i in range(3):
    burger = int(input())
    b.append(burger)

for i in range(2):
    drink = int(input())
    d.append(drink)

print(min(b)+min(d)-50)
