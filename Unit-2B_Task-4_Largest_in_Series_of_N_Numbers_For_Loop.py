n=int(input('Enter the count: '))
if n>0:
m=float(input('Enter the number: '))
for i in range(n-1):
x=float(input('Enter the number: '))
if x>m: m=x
print('Largest:',m)
else: print('No numbers')
