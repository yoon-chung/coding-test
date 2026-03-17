import sys
input = sys.stdin.readline

n = int(input())
arrow = {} # dictionary
ans = 0
for h in map(int, input().split()):
    if arrow.get(h, 0): # dict.get(x, y)
        arrow[h] -= 1   # x인덱스에 해당하는 값이 존재하면 dict[x]를 반환, 없는 경우 y를 반환
    else: # python은 0을 False로 판정합니다.
        ans += 1

    arrow[h-1] = arrow.get(h-1, 0) + 1
    # 딕셔너리의 get(a, b) 메소드는 해당 딕셔너리에서
    # key가 a인 value가 존재하면 해당 값을, 존재하지 않을 때는 b를 반환합니다.

print(ans)