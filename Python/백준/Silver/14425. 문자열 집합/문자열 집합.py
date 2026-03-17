import sys
input = sys.stdin.readline

N, M = map(int, input().split())

S = set([])
for _ in range(N):
    S.add(input().rstrip())   # rstrip: 오른쪽 공백 모두 제거

answer = 0
for _ in range(M):
    answer += 1 if input().rstrip() in S else 0

print(answer)