lista = [2, 4, 6, 8, 10]

def is_in(x):
	result = False
	for i in lista:
		if x == i:
			result = True
	return print(f'{x} => {result}')

print(lista)
is_in(5)
is_in(10)


#2

def is_in(x):
  result = False
  if x in lista:
    result = True
  return print(f'{x} => {result}')
