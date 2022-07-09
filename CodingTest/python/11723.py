import sys
m = int(sys.stdin.readline())

s = set()
for _ in range(m):
    x = sys.stdin.readline().strip().split()

    if(len(x) == 1):
        if(x[0] == "all"):
            s = set([i for i in range(1, 21)])
        else:
            s = set()  # empty일 경우
    else:
        command, n = x[0], x[1]
        n = int(n)

        if command == "add":
            s.add(n)
        elif command == "remove":
            s.discard(n)
        elif command == "check":
            if n in s:
                print("1")
            else:
                print("0")
        elif command == "toggle":
            if n in s:
                s.discard(n)
            else:
                s.add(n)
