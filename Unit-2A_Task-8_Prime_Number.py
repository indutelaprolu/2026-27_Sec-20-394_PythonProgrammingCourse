n=int(input('Enter the number: '))
i=2
prime=n>=2
while i<n:
if n%i==0: prime=False
i+=1
print('Prime' if prime else 'Not prime')
