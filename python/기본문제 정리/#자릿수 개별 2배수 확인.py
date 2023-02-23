result = list()
for i in range(100,300):
	test = (list(str(i)))
	if (int(test[0]) == 0 or int(test[0]) % 2 == 0) and \
		(int(test[1]) == 0 or int(test[1]) % 2 == 0) and \
		(int(test[2]) == 0 or int(test[2]) % 2 == 0):
		result.append(i)
print(','.join(map(str, result)))


## chatGPT
result = []
for i in range(100, 301):
    digits = [int(d) for d in str(i)]  # 각 자리수를 리스트로 분리
    if all(digit % 2 == 0 for digit in digits):  # 모든 자리수가 짝수인지 검사
        result.append(str(i))

print(",".join(result))