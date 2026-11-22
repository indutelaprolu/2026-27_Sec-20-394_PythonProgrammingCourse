n=int(input('Enter the count: '))
s=0
for i in range(n): s+=float(input('Enter the value: '))
print('Sum =',s)
if n>0: print('Average =',s/n)
else: print('No values')
