temp0 = 1
temp1 = 2
temp2 = temp0+temp1
DATA = 0
while (temp0 <= 4e6):
    temp2 = temp0+temp1
    if (temp0%2==0):
        DATA+=temp0
    temp0=temp1
    temp1=temp2
print(DATA)
