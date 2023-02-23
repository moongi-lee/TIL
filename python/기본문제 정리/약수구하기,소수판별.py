x = int(input())
x_list = []
for i in range(1, x+1):
	if x % i == 0:
		x_list.append(i)
for i in x_list:
	print(f'{i}(은)는 {x}의 약수입니다.')
if len(x_list) == 2:
	print(f'{x}(은)는 {x_list[0]}과 {x_list[1]}로만 나눌 수 있는 소수입니다.')



#2
x = int(input())
y = list()
for i in range(1, x+1):
	if x % i == 0:
		y.append(i)
if len(y) == 2:
	print('소수입니다.')
