# EXAMPLES

# Input
# Masukkan angka : 68
# Expected result
# Angka 68 adalah bilangan genap

# Input
# Masukkan angka : 21
# Expected result
# Angka 21 adalah bilangan ganjil

nomor = int(input('Masukan Bilangan : '))

if nomor %2 == 0:
    print  ('%i adalah sebuah genap' % nomor)
else: 
    print ('%i adalah sebuah bilangan ganjil' % nomor)
