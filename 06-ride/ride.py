"""
ID: mrcream1
LANG: PYTHON3
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
x = fin.readline().strip()
y = fin.readline().strip()
com = 1
hvn = 1
for i in x:
    com *= (ord(i)-64)
for j in y:
    hvn *= (ord(j)-64)
if (com%47 == hvn%47):
    fout.write('GO'+ '\n')
else:
    fout.write('STAY'+ '\n')
fout.close()


