x = int(input())
pibo_list = []
for i in range(x):
	if i in (0,1):
		pibo_list.append(1)
	else:
		pibo_list.append(pibo_list[i-2] + pibo_list[i-1])
print(pibo_list)



# chatGPT

def fibonacci(n):
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-1] + fib[-2])
    return fib

print(fibonacci(10))