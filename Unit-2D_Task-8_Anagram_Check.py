a=input('Enter the first string: ').lower().replace(' ','')
b=input('Enter the second string: ').lower().replace(' ','')
print('Anagrams' if sorted(a)==sorted(b) else 'Not anagrams')
