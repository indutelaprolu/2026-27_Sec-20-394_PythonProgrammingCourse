n=int(input('Enter the number: '))
p=n>=2
for i in range(2,n):
if n%i==0: p=False; break
print('Prime' if p else 'Not prime')
