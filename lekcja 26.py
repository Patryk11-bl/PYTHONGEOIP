import copy
oceny = [1,2,3,4,5,6,1,2,3,4,5,6,5,4,3,2,1,6]
nowe_oceny = []

for e in oceny:
    if e == 4:
        e=3
    elif e ==2:
        e =1
    elif e ==5:
        e= 3
        
        
    elif e == 6:
        e =4
    nowe_oceny.append(e)

print(nowe_oceny)