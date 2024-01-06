data = (5, 9, 7, 8, 7)
for i in range(len(data)):
    print("Data  ke-",i," = ", data[i])

for i in data:
    print(i)

# set

s1 = set({})
print(s1)

data = {5, 9, 7, 8, 7}
for i in data:
    print(i)


anggota = set({}) # set kosong
print(anggota)
anggota.add("ade")
print(anggota)
anggota.add("budi")
print(anggota)
anggota.update(["cepi","erni",""])
print(anggota)

print(())

mhs = {'nama'  : 'Budi',
       'umur'  : 21,
       'kota'  : 'Bandung'
       }
for key in mhs:
    print(key)
print("----------------")
for key in mhs:
    print(key, '=>', mhs[key])


