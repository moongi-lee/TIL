def count_down(x):
	if x == 0:
		return print("카운트다운을 하려면 0보다 큰 입력이 필요합니다.")
	else:
		for i in range(x,0,-1):
    #for i in reversed(range(x))
			print(i)

count_down(0)
count_down(10)
