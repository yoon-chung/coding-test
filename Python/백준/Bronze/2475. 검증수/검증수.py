a, b, c, d, e = map(int, input().split())
list = [a,b,c,d,e]
ans = 0
for i in list:
    ans += i**2
print(ans%10)