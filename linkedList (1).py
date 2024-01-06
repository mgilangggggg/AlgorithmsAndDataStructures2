# 1. pendefinisan Struktur Data Linked List
# Class untuk Node
from cmath import phase
from select import select

class Data:
    def __init__(self, info):
        self.info = info
        self.next = None

# Class untuk Linked List


class LinkedList:
    def __init__(self):
        self.awal = None

    def isEmpty(self):
        return self.awal is None

    def TampilData(self):
        print('Isi Linked List : ', end="")
        if self.isEmpty():
            print('Data Kosong')
        else:
            bantu = self.awal
            while bantu is not None:
                print(bantu.info, "", end="")
                if (bantu.next is not None):
                    print("-> ", end="")
                bantu = bantu.next
            print()

    def BanyakNode(self):
        if self.isEmpty():
            byknode = 0
        else:
            bantu = self.awal
            byknode = 0
            while bantu is not None:
                byknode = byknode + 1
                bantu = bantu.next

        return byknode

    def Penghancuran(self):
        Phapus = self.awal
        while (Phapus is not None):
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

# Operasi Pencarian
# Pencarian Data
    def PencarianAngka(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            CariAngka = int(input('Masukkan Angka yang Dicari :'))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info == CariAngka):
                    ketemu = True
                else:
                    bantu = bantu.next

            if (ketemu):
                print('Angka', CariAngka, 'Ditemukan')
            else:
                print('Angka', CariAngka, 'Tidak ditemukan')

# Pencarian Node
    def PencarianNode(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            CariNode = int(input('Masukkan Node yang Dicari :'))
            bantu = self.awal
            ketemu = False
            posisi = 1
            while (not ketemu) and (bantu is not None):
                if (posisi == CariNode):
                    ketemu = True
                else:
                    bantu = bantu.next
                    posisi += 1

            if (ketemu):
                print('Node ke-', CariNode, 'Ditemukan')
            else:
                print('Node ke-', CariNode, 'Tidak ditemukan')

# Operasi Penambahan Data
# Penambahan Depan
    def SisipDepanSingle(self, DataBaru):
        Baru = Data(DataBaru)
        if (not self.isEmpty()):
            Baru.next = self.awal

        self.awal = Baru
# Penambahan Belakang

    def SisipBelakangSingle(self, DataBaru):
        Baru = Data(DataBaru)
        if (self.isEmpty()):
            self.awal = Baru
        else:
            bantu = self.awal
            while (bantu.next is not None):
                bantu = bantu.next

        bantu.next = Baru
# Penambahan Tengah (Sisip)

    def SisipTengahSingle(self, DataBaru):
        SisipSetelah = int(input('Masukkan Angka yang Dicari :'))
        bantu = self.awal
        ketemu = False
        while (not ketemu) and (bantu is not None):
            if (bantu.info == SisipSetelah):
                ketemu = True
            else:
                bantu = bantu.next

        if (ketemu):
            Baru = Data(DataBaru)
            if (bantu.next in None):
                self.SisipBelakangSingle(DataBaru)
            else:
                Baru.next = bantu.next
                bantu.next = Baru

        else:
            print('Angka', SisipSetelah, 'Tidak ditemukan')


# Operasi Pengubahan Data

    def UbahData(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            CariUbah = int(input('Masukkan Angka yang Dicari :'))
            bantu = self.awal
            ketemu = False
            while (not ketemu) and (bantu is not None):
                if (bantu.info == CariUbah):
                    ketemu = True
                else:
                    bantu = bantu.next

            if (ketemu):
                DataBaru = int(input('Masukkan Data Perubah : '))
                bantu.info = DataBaru
            else:
                print('Angka', CariUbah, 'Tidak ditemukan')

# Operasi Penghapusan Data
    def SatuNode(self):
        bantu = self.awal
        if(bantu.next is None):
            return True
        else:
            return False

# Penghapusan Depan
    def HapusDepanSingle(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.awal
            Elemen = Phapus.info
            if (self.SatuNode()):
                self.awal = None
            else:
                self.awal = Phapus.next

            del Phapus
            print('Data yang Dihapus Adalah : ', Elemen)

# Penghapusan Belakang
    def HapusBelakangSingle(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.awal
            if (self.SatuNode()):
                self.awal = None
            else:
                # Pencarian Node Terakhir
                while (Phapus.next is not None):
                    Phapus = Phapus.next

                # Pencarian Node Sebelum Node Terakhir
                bantu = self.awal
                while (bantu.next is not Phapus):
                    bantu = bantu.next

                bantu.next = None
            Elemen = Phapus.info
            del Phapus
            print('Data yang Dihapus Adalah : ', Elemen)

# Penghapusan Tengah
    def HapusTengahSingle(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            DataHapus = int(input('Masukkan Angka yang Akan Dihapus : '))
            Phapus = self.awal
            ketemu = False
            while (not ketemu) and (Phapus is not None):
                if (Phapus.info == DataHapus):
                    ketemu = True
                else:
                    Phapus = Phapus.next

            if (ketemu):
                Elemen = Phapus.info
                if(Phapus == self.awal):
                    self.HapusDepanSingle()
                elif (Phapus.next is None):
                    self.HapusBelakangSingle()
                else:
                    bantu = self.awal
                    while (bantu.next is not Phapus):
                        bantu = bantu.next

                    bantu.next = Phapus.next

                    del Phapus
                    print('Data yang Dihapus Adalah : ', Elemen)
            else:
                print('Angka', DataHapus, 'Tidak ditemukan')


# Pengurutan Data Secara Ascending Menggunakan Minimum Sort

    def UrutData(self):
        i = self.awal
        while (i.next is not None):
            min = i
            j = i.next
            while (j is not None):
                if(j.info < min.info):
                    min = j
                j = j.next

                # Proses Pertukaran
                temp = min.info
                min.info = i.info
                i.info = temp

                # Tempatkan i ke simpul berikutnya
                i = i.next


# 2. Inisialisasi Linked List
point = LinkedList()
print('Awal Linked List :', point.awal)

# 3. Memasukkan Data ke Linked List Secara Langsung
node1 = Data(5)
node2 = Data(11)
node3 = Data(3)
node4 = Data(7)

# print('Isi Node 1 : ', node1.info, '-', node1.next)
# print('Isi Node 2 : ', node2.info, '-', node3.next)

# Membuat Linked List
point.awal = node1
node1.next = node2
node2.next = node3
node3.next = node4

print('Isi Node 1 : ', node1.info, '-', node1.next)
print('Isi Node 2 : ', node2.info, '-', node3.next)

# 4. Transversal Untuk Menampilkan Data
point.TampilData()

# 5. Transversal Untuk Menghitung Banyak Data
print('Banyak Data : ', point.BanyakNode())

# 7. Operasi Pencarian
# Pencarian Data
# point.PencarianAngka()

# Pencarian Node
# point.PencarianNode()

# 8. Operasi Penambahan
# DataBaru = int(input('Masukkan data Baru : '))

# Penambahan Depan
# point.SisipDepanSingle(DataBaru);

# Penambahan Belakang
# point.SisipBelakangSingle(DataBaru);

# Penambahan Tengah (Sisip)
# point.SisipTengahSingle(DataBaru);

# 9. OPerasi Pengubahan
# point.UbahData()

# 10. Operasi Penghapusan
# Penghapuasan Depan
# point.HapusDepanSingle()
# Penghapuasn Belakang
# point.HapusBelakangSingle()
# Penghapusan Tengah
# point.HapusTengahSingle()


# 11. Pengurutan Data
if (point.isEmpty()):
    print('Data Kosong')
else:
    point.UrutData()

point.TampilData()

# 6. Penghancuran Linked List
point.Penghancuran()
# point.TampilData()
# print('Banyak Data : ', point.BanyakNode())