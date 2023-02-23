x = input()
list = ['0','1','2','3','4','5','6','7','8','9']
print('0 1 2 3 4 5 6 7 8 9')
for i in list:
	if x.count(i) == 0:
		print('0', end=' ')
	else:
		print(x.count(i), end=' ')
  
  
# chatGPT
number = int(input("양의 정수를 입력하세요: "))
digits = [0] * 10

while number > 0:
    digit = number % 10
    digits[digit] += 1
    number //= 10

print("각 숫자의 사용 횟수:")
for i in range(10):
    print("{}: {}".format(i, digits[i]))
    