# 1. Pendefinisian Stuktur Data Linked List
# Class Untuk Node
from asyncio import base_events
from cmath import phase
from ctypes import BigEndianStructure
from curses import baudrate
from sqlite3 import enable_shared_cache
from xml.dom.minidom import Element


class Data:
    def __init__(self, info):
        self.info = info
        self.next = None

# Class Untuk Linked List


class LinkedList:
    def __init__(self):
        self.awal = None

    def IsEmpty(self):
        return self.awal is None

    def TampilData(self):
        print('Isi Linked List : ', end="")
        if self.IsEmpty():
            print('Data Kosong')
        else:
            bantu = self.awal
            while bantu is not None:
                print(bantu.info, "", end="")
                if (bantu.next is not None):
                    print("->", end="")
                bantu = bantu.next
            print()

    def BanyakNode(self):
        if self.IsEmpty():
            banyaknode = 0
        else:
            bantu = self.awal
            banyaknode = 0
            while bantu is not None:
                banyaknode = banyaknode + 1
                bantu = bantu.next
        return banyaknode

    def Penghacuran(self):
        Phapus = self.awal
        while (Phapus is not None):
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

# Operasi Pencarian
# Pencarian Data
    def PencarianAngka(self):
        if (self.IsEmpty()):
            print('Data Kosong')
            else:
                CariAngka = int(input('Masukan Angka Yang Dicari : '))
                bantu = self.awal
                ketemu = False
                while (not ketemu) and (bantu is not None):
                    if (bantu.info == CariAngka):
                    ketemu = True
                else:
                    bantu = bantu.next

                if (ketemu):
                    print('Angka ', CariAngka, 'Ditemukan')
                else:
                    print('Angka', CariAngka, 'Tidak Ditemukan')

# Operasi Node
    def pencarianNode(self):
        if (self.IsEmpty()):
            print('Data Kosong')
            else:
                CariNode = int(input('Masukan Node Yang Dicari : '))
                bantu = self.awal
                ketemu = False
                posisi = 1
                while (not ketemu) and (bantu is not None):
                    if (posisi.info == CariNode):
                    ketemu = True
                else:
                    bantu = bantu.next

                if (ketemu):
                    print('Node Ke- ', CariNode, 'Ditemukan')
                else:
                    print('Node Ke-', CariNode, 'Tidak Ditemukan')

# Operasi Penambahan Data
# Penambahan Depan
    def SisipDepanSingle(self, DataBaru):
        Baru = Node(DataBaru):
        if (not self.IsEmpty()):
            Baru.next = self.awal

        self.awal = Baru

# Penambahan Belakang
    def SisipBelakangSingle(self, DataBaru):
        Baru = Node(DataBaru)
        if (self.IsEmpty()):
            self.awal = Baru
        else:
            bantu = bantu.next
            while (bantu.next is not None):
                bantu = bantu.next

        bantu.next = Baru

# Penambahan Tengah (Sisip)
    def SisipTengahSigle(self, DataBaru):
        SisipSetelah = int(input('Sisipkan Setelah : '))
        bantu = self.awal
        ketemu = False
        while (not ketemu) and (bantu is not None):
            if (bantu.info == CariAngka):
                ketemu = True
        else:
            bantu = bantu.next

        if (ketemu):
            Baru = Node(DataBaru)
            if (bantu.next is None):
                self.SisipBelakangSingle(DataBaru)
            else:
                Bantu.next = bantu.next
                bantu.next = Baru
        else:
            print('Angka', CariAngka, 'Tidak Ditemukan')

# Operasi Pengubahan Data


def UbahData(self):
        if (self.IsEmpty()):
            print('Data Kosong')
            else:
                CariUbah = int(input('Masukan Angka Yang Ingin Diubah : '))
                bantu = self.awal
                ketemu = False
                while (not ketemu) and (bantu is not None):
                    if (bantu.info == CariUbah):
                    ketemu = True
                else:
                    bantu = bantu.next

                if (ketemu):
                    DataBAru = int(input('Masukan Data Ubah'))
                    bantu.info = DataBaru
                else:
                    print('DataBaru', CariUbah, 'Tidak Ditemukan')


# Operasi Penghapusan Data
    def SatuNode(self):
        bantu = self.awal
        if(bantu.next is None):
            return True
        else :
            return False

# Operasi Penghapusan Depan
    def HapusDepanSingle (self):
        if(self.isEmpty()):
            print('DAta Kosong')
        else :
            Phapus = self.awal
            Elemen = Phapus.info
            if(self.SatuNode()):
                self.awal = None
            else :
                self.awal = Phapus.next

            del Phapus
            print('Data yang Dihapus Adalah : ',Elemen)

# Operasi Penghapusan Belakang
    def HapusBelakangSingle (self):
        if(self.IsEmpty()):
            print('Data Kosong')
        else :
            if(self.SatuNode()):
                self.awal = None
            else :
                # Pencarian Node Terakhir
                while (Phapus.next is not None):
                    Phapus = Phapus.next

                # Pencarian Node Sebelum Node Terakhir
                bantu = self.awal
                while (bantu.next is not Phapus):
                    bantu = bantu.next

                    Bantu.next


# Operasi Penghapusan Tengah
     def HapusTengahSingle(self):
        if (self.IsEmpty()):
            print('Data Kosong')
        else:
                DataHapus = int(input('Masukan Angka Yang Akan Dihapus : '))
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
                    elif(Phapus.next is not Phapus):
                        self.HapusBelakangSingle()
                    else :
                        bantu = self.awal
                        while (bantu.next is not Phapus):
                            bantu = bantu.next

                        bantu.next = Phapus.next

                        del Phapus
                        print ('Data Yang Dihapus Adalah : ',Elemen)
                else:
                    print('Angka', DataHapus, 'Tidak Ditemukan')

# Secara Ascending Minimus Sort
    def UrutData(self):
        i = self.awal
        while(i.next is not None):
            min = i
            j = i.next
            while (j i not None):
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
print('Awal Linked List : ', point.awal)

# 3. Memasukan Data ke List Secara Langsung
node1 = Data(5)
node2 = Data(7)
node3 = Data(11)
node4 = Data(2)

# print('Isi Node 1 : ', node1.info, '-', node1.next)
# print('Isi Node 2 : ', node3.info, '-', node4.next)

# Membuat Linked List
point.awal = node1
node1.next = node2
node2.next = node3
node3.next = node4

# print('Isi Node 1 : ', node1.info, '-', node1.next)
# print('Isi Node 2 : ', node3.info, '-', node2.next)

# 4. Traversal Untuk Menampilkan Data
point.TampilData()

# 5. Traversal Untuk Banyak Data
# print('Banyak Data : ', point.BanyakNode())

# 7. Operasi Pencarian
# Pencarian Data
# list1.PencarianAngka

# 8. Operasi Penambahan
DataBaru = int(input('Masukan Data Baru : '))

# Penambahan Depan
# list1.SisipDepanSingle(DataBaru)

# Penambahan Belakang
# list1.SisipBelakang
# 6. Penghancuran Linked List
point.Penghacuran()
# point.TampilData()
# print('Banyak Data : ', point.BanyakNode())
