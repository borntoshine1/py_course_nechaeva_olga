a = int(input('Enter a: '))
b = int(input('Enter b: '))
if a>0 or a<0:
    x = -b/a
    print('x value is - {}'.format(x))
elif a == 0 and b == 0:
    print('X any value')
else:
    print('No solutions')
