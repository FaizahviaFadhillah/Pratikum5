no = 0
lanjut = 'y'
nama = []
nim = []
uts = []
uas = []
tugas = []
akhir = []
while lanjut == 'y':
    nam = str(input('Nama\t\t: '))
    ni = int(input('Nim\t\t: '))
    tugs = int(input('Nilai Tugas\t: '))
    ut = int(input('Nilai UTS\t: '))
    us = int(input('Nilai UAS\t: '))
    akhr = float(tugs*0.3)+(ut*0.35)+(us*0.35)
    tugas.append(tugs)
    nama.append(nam)
    nim.append(ni)
    uts.append(us)
    uas.append(us)
    akhir.append(akhr)
    no +=1
    lanjut = input('tambah data (y/t)? ')

print('========================================================')
print('|NO |   Nama    |    NIM    |Tugas| UTS | UAS | Akhir |')
print('========================================================')
for i in range (no):
        print('|',i+1,'|  ',nama[i],'  |',nim[i],'|',tugas[i],' | '
        ,uts[i],'| ',uas[i],'|',round(akhir[i],2),'|')
print('========================================================')



