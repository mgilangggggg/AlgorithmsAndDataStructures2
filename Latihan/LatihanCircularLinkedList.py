# 1. Pendefinisian Sturktur Data Linked List
# Class Untuk Node
class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
        self.prev = None

# Class Untuk Linked List
class DoubleCircularLinkedList:
    def __init__(self):
        self.awal = None
        self.akhir = None

    def isEmpty(self):
        return self.awal is None

    def TampilData(self):
        print('Isi Linked List :', end=' ')
        if self.isEmpty():
            print('Data Kosong')
        else:
            bantu = self.awal
            while (bantu != self.akhir):
                print(bantu.info, '', end='')
                if bantu.next is not None:
                    print('->', end=' ')
                bantu = bantu.next
            print(bantu.info) #Menampilkan Node Akhir
            print()

    def TampilData2(self):
            print('Isi Linked List :', end=' ')
            if self.isEmpty():
                print('Data Kosong')
            else:
                bantu = self.akhir
                while (bantu != self.awal):
                    print(bantu.info, '', end='')
                    if bantu.prev is not None:
                        print('->', end=' ')
                    bantu = bantu.prev
                print(bantu.info) #Manampilkan Node Awal
                print()

    def Penghancuran(self):
        Phapus = self.awal
        while (Phapus != self.akhir):
            self.awal = Phapus.next
            self.awal.prev = self.akhir
            self.akhir.next = self.awal
            del Phapus
            Phapus = self.awal
        self.awal = None
        self.akhir = None
        del Phapus

# Operasi Penambahan
# Penambahan di Awal
    def SisipDepanCircularDouble (self, DataBaru):
        Baru = Node(DataBaru)
        if (self.isEmpty()):
            self.akhir = Baru
        else:
            Baru.next = self.awal
            self.awal.prev = Baru
        self.awal = Baru
        # Penambahan Untuk Circular
        self.awal.prev = self.akhir
        self.akhir.next = self.awal

# Penambahan di Belakang
    def SisipBelakangCircularDouble (self, DataBaru):
        Baru = Node(DataBaru)
        if(self.isEmpty()):
            self.awal = Baru
        else:
            Baru.prev = self.akhir
            self.akhir.next = Baru
        self.akhir = Baru
        # Penambahan Untuk Circular
        self.awal.prev = self.akhir
        self.akhir.next = self.awal

# Penambahan di Tengah (Sisip)
    def SisipTengahCircularDouble(self, DataBaru):
        SisipSetelah = int(input('Sisipkan Setelah : '))
        bantu = self.awal
        while (bantu.info != SisipSetelah) and (bantu != self.akhir):
            bantu = bantu.next

        if(bantu.info == SisipSetelah):
            if(bantu == self.akhir):
                self.SisipBelakangCircularDouble(DataBaru)
            else:
                Baru = Node(DataBaru)
                Baru.next = bantu.next
                Baru.prev = bantu
                bantu.next.prev = Baru
                bantu.next = Baru
        else:
            print('Data',SisipSetelah,'Tidak Ditemukan')

# Operasi Penghapusan
    def SatuNode (self):
        if (self.awal == self.akhir):
            return True
        else:
            return False
# Penghapusan Depan
    def HapusDepanCircularDouble(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.awal
            Elemen = Phapus.info
            if(self.SatuNode()):
                self.awal = None
                self.akhir = None
            else:
                self.awal = Phapus.next
                self.awal.prev = self.akhir
                self.akhir.next = self.awal

            del Phapus
            print('Data yang Dihapus Adalah : ',Elemen)

# Penghapusan Belakang
    def HapusBelakangCircularDouble(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            Phapus = self.akhir
            Elemen = Phapus.info
            if(self.SatuNode()):
                self.awal = None
                self.akhir = None
            else:
              self.akhir = Phapus.prev
              self.akhir.next = self.awal
              self.awal.prev = self.akhir

        del Phapus
        print('Data Yang Dihapus Adalah : ', Elemen)

#Penghapusan Di Tengah
    def HapusTengahCircularDouble(self):
        if (self.isEmpty()):
            print('Data Kosong')
        else:
            DataHapus = int(input('Masukan Data Yang Akan Dihapus : '))
            Phapus = self.awal
            while (Phapus.info != DataHapus) and (Phapus != self.akhir):
                Phapus = Phapus.next

            if (Phapus.info == DataHapus):
                Elemen = Phapus.info
                if (Phapus == self.akhir):
                    self.HapusBelakangCircularDouble()
                elif (Phapus == self.awal):
                    self.HapusDepanCircularDouble()
                else:
                   Phapus.prev.next = Phapus.next
                   Phapus.next.prev = Phapus.prev
                   
                del Phapus
                print('Data Yang Dihapus Adalah :',Elemen)
                
            else:
                print('Data',DataHapus,'Yang Akan Dihapus Tidak Ada')

# Pengurutan Data Secara Ascending Menggunakan Minimum Sort
    def UrutDataAsc(self):
        i = self.awal
        while (i.next != self.akhir):
            min = i
            j = i.next
            while (j != self.akhir):
                if (j.info < min.info):
                    min = j
                j = j.next

            if (j.info < min.info): #Membandingkan dengan node terakhir
                    min = j
            # Proses Pertukan dua Buah Data
            temp = min.info
            min.info = i.info
            i.info = temp

            # Menempatkan Pointer i ke simpul berikutnya
            i = i.next

            min = i
            j = i.next
            if (j.info < min.info): #Membandingkan dengan node terakhir
                    min = j
            # Proses Pertukan dua Buah Data
            temp = min.info
            min.info = i.info
            i.info = temp

# 2. Inisialisasi Linked List
list1 = DoubleCircularLinkedList()
# print('Awal Linked List :',list.awal)

# 3. Memasukan Data Ke linked list Secara Langsung
node1 = Node(5)
node2 = Node(7)
node3 = Node(2)
node4 = Node(10)

# Membuat Linked List
# list1.awal = node1
# node1.next = node2
# node2.next = node3
# node2.prev = node1
# node3.next = node4
# node3.prev = node2
# node4.prev = node3
# list1.akhir = node4

# print('Isi Node 1 : ', node1.prev, '-', node1.info, '-', node1.next)
# print('Isi Node 2 : ', node2.prev, '-', node2.info, '-', node2.next)
# print('Isi Node 3 : ', node3.prev, '-', node3.info, '-', node3.next)
# print('Isi Node 4 : ', node4.prev, '-', node4.info, '-', node4.next)

print('--Menu--')
print('1. Tambah Data')
print('2. Hapus Data')
print('3. Tampil Data')
print('4. Pengurutan Data')
print('0. keluar')
menu = int(input('Masukan Pilihan menu : '))

while (menu != 0):
    if(menu == 1):
        DataBaru = int(input('Masukan Data Baru : '))
        if (list1.isEmpty()):
            list1.SisipDepanCircularDouble(DataBaru)
        else:
            print('1. Sisip Depan')
            print('2. Sisip Belakang')
            print('3. Sisip Tengah')
            menu2 = int(input('Masukan Pilihan Tambah : '))
            if (menu2 == 1):
                list1.SisipDepanCircularDouble(DataBaru)
            elif(menu2 == 2):
                list1.SisipBelakangCircularDouble(DataBaru)
            elif(menu2 == 3):
                list1.SisipTengahCircularDouble(DataBaru)
            else:
                print('Menu Tambah Tidak Ada')
        list1.TampilData()

    elif(menu == 2):
        print('1. Hapus Depan')
        print('2. Hapus Belakang')
        print('3. Hapus Tengah')
        menu2 = int(input('Masukan Pilihan Hapus : '))
        if (menu2 == 1):
            list1.HapusDepanCircularDouble()
        elif(menu2 == 2):
            list1.HapusBelakangCircularDouble()
        elif(menu2 == 3):
            list1.HapusTengahCircularDouble()
        else:
            print('Menu Hapus Tidak Ada')
        list1.TampilData()

    elif(menu == 3):
        print('Tampil Data Dari Depan')
        list1.TampilData()
        print()
        print('Tampil Data Dari belakang')
        list1.TampilData2()
    elif(menu == 4):
        print('Data Sebelum Di Urutkan')
        list1.TampilData()
        print()
        print('Data Setelah Di Urutkan')
        list1.UrutDataAsc()
        list1.TampilData()
    else:
        print('Pilihan Menu Tidak Ada')

    print()
    print('--Menu--')
    print('1. Tambah Data')
    print('2. Hapus Data')
    print('3. Tampil Data')
    print('4. Pengurutan Data')
    print('0. keluar')
    menu = int(input('Masukan Pilihan menu : '))
else:
    print('Terima Kasih')
    list1.Penghancuran()
