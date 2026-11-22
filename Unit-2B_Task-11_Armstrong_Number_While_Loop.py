n=int(input('Enter the three-digit number: '))
x=n;s=0
while x>0:
    d=x%10; s+=d**3; x//=10
print('Armstrong' if s==n else 'Not Armstrong')
