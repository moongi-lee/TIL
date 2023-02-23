def change(x):
	if x == '가위':
		return 0
	elif x == '바위':
		return 1
	elif x == '보':
		return 2

Man1 = change(input())
Man2 = change(input())

if (Man1 - Man2) == 0:
	print('Result : Draw')
elif (Man1 - Man2) in [1,-2]:
	print('Result : Man1 Win!')
else:
	print('Result : Man2 Win!')

# 2번째
def change(x):
	if x == '가위':
		return 0
	elif x == '바위':
		return 1
	elif x == '보':
		return 2

def rule(x,y):
	if change(x) - change(y) == 0:
		print('비겼습니다.')
	elif change(x) - change(y) in (1,-2):
		print(f'{x}가 이겼습니다!')
	else:
		print(f'{y}가 이겼습니다!')

x = input()
x = input()

rule(input(),input())