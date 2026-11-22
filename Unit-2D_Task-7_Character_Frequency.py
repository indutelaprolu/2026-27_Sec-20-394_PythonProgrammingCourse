s=input('Enter the string: ')
f={}
for ch in s:
    f[ch]=f.get(ch,0)+1
for ch,count in f.items(): print(ch,':',count)
