#Donavan Bryant using list len, max, min, and sum

print('Rainfall for Chicago (2017):')
numb=[0]*12
for x in range (0,12):
    print(x)
    numb[x]=float(input('Enter rainfall:'))
    
len01=len(numb)
print(numb)
print('Highest rainfall->',max(numb))
print('Lowest rainfall->',min(numb))
print('Total rainfall->',sum(numb))
a=sum(numb)/12
print('Average is',a)


