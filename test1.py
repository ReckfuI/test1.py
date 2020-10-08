n = input('Insert the number : ')
n = int(n)
print('Selected number', n )
for i in range(n):
    n = ''
    if (i % 3 == 0):
        n+='Fizz'
    if (i % 5 == 0):
        n+='Buzz'
        print(n)
