j = [ 80, 50, 24, 10, 30]
print(j)
print(j[2])
print(j[1:4])
print(j[4])

print('===============================')

j[4] = 200
print(j[4])
j[3:] = 36, 71
print(j[3:4])

print('===============================')

k = j[0:2]
print (k)
k.append(41)
print (k)
k.extend([70, 90, 100])
print (k)
l = j + k
print (l)

