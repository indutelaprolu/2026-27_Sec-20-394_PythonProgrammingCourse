n=abs(int(input('Enter the number: ')))
c=1 if n==0 else 0
while n>0:
    c+=1; n//=10
print('Digits =',c)
