n = int(input())
number = []
while n > 0:
    q = n % 10
    number.append(q)
    n = n // 10

number.reverse()
# print(number)

for j in number:
    print(str(j), " :", str(j) * j)