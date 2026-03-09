#10 20 30 입력 시 a=10, b=20, c=30 (정수)로 저장
#input()으로 문자열을 받고, split()으로 나눈 뒤, map()을 통해 모두 숫자로
a, b, c = map(int, input().split())

# a**b mod c
print(pow(a, b, c))

