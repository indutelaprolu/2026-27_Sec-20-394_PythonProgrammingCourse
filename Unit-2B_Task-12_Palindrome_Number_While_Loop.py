n=int(input('Enter the number: '))
x=n; rev=0
while x>0:
    rev=rev*10+x%10; x//=10
print('Palindrome' if n>=0 and n==rev else 'Not palindrome')
