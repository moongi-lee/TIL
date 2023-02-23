x = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
result = 0
while len(x) > 0:
	y = x.pop()
	if y >= 80:
		result += y
print(result)


# chhatGPT
scores = [85, 65, 77, 83, 75, 22, 98, 88, 38, 100]
total = 0

while scores:   # scores 원소가 없어지면 false 가 되므로 자동으로 멈춤
    score = scores.pop()
    if score >= 80:
        total += score

print(total)