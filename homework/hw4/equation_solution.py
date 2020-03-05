a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a>0 and b>=0:
	x = -b/a
	print('x value is - ' + str(x))
elif a == 0:
	print('No solutions')
	