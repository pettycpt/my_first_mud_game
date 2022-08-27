n = '11  l,j'
shuzi = 0
kongge = 0
zimu = 0
qita = 0
for i in n:
    if i.isalpha():
        shuzi += 1
    elif i.isdigit():
        zimu += 1
    elif i.isspace():
        kongge += 1
    else:
        qita += 1
print(zimu)
print(shuzi)
print(kongge)
print(qita)