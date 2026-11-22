n=int(input('Enter the number: '))
sign=-1 if n<0 else 1
x=abs(n); rev=0
while x>0:
    rev=rev*10+x%10; x//=10
print('Reverse =',sign*rev)
