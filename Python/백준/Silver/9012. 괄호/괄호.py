import sys
input = sys.stdin.readline
def isVPS(line):
    stack = []
    for x in line:
        try:
            if x=='(':
                stack.append(x)
            else:
                stack.pop()
        except IndexError:
            return 'NO'
    return 'NO' if stack else 'YES'

t = int(input())
for _ in range(t):
    print(isVPS(input().rstrip()))