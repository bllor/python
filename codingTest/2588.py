a= 472
b = '385'
print(len(b))

for i in range(len(b)-1,-1,-1):
    print(a*int(b[i]))
print(a*int(b))