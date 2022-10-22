a = float(input('1 коэф '))
b = float(input('2 коэф '))
c = float(input('3 коэф '))
dis = b**2 - 4*a*c
if dis < 0:
    print('Решения нет.⌀')
elif dis == 0:
    x = (-b)/(2*a)
    print('Ответ',x)
else:
    x1 = ((-b)+(dis**0.5))/(2*a)
    x2 = ((-b)-(dis**0.5))/(2*a)
    print('Ответ:','X1:',x1,'X2:',x2)