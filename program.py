print('program1.py')

a = 100000000

for x in range(1,9):
  if (x>=1 and x<=2):
    b=a*0
    print('laba bulanan ke-',x,':',b)

  if (x>=3 and x<=4):
    c=a*0.1
    print('laba bulanan ke-',x,':',c)

  if (x>=5 and x<=7) :
    d=a*0.5
    print('laba bulanan ke-',x,':',d)
    

  if (x==8) :
    e=a*0.2
    print('laba bulanan ke-',x,':',e)

total = b+b+c+c+d+d+e
print('\nTotal : ', total)