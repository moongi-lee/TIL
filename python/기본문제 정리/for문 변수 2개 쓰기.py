x = [(1,88),(2,30),(3,61),(4,55),(5,95)]

for i, j in x:
	if j >= 60:
		print(f'{i}번 학생은 {j}점으로 합격입니다.')
	else:
		print(f'{i}번 학생은 {j}점으로 불합격입니다.')