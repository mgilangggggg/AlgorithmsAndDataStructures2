# 1. Pendefinisian Struktur Data Linked List
# Class Untuk Node
class Data:
    def _init_(self, info):
        self.info = info
        self.next = None
        self.prev = None

# Class Untuk Linked List

class DoubleLinkedList:
    def _init_(self):
        self.awal = None
        self.akhir = None

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
                if(bantu.next is not None):
                    print("->", end="")
                bantu = bantu.next
            print()

    def Penghancuran(self):
        Phapus = self.awal
        while Phapus is not None:
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal
        self.akhir = None


# 2. Inisialisasi Linked List
list1 = DoubleLinkedList()
# print("Awal Linked List: ", point.awal)

# 3. Memasukan Data Ke Linked List Secara Langsung
node1 = Data(5)
node2 = Data(7)
node3 = Data(2)
node4 = Data(10)

# print("Isi Node 1 : " , node1.info,"-", node1.next)
# print("Isi Node 2 : " , node2.info,"-", node2.next)

# Membuat Linked List
# list1.awal = node1
# node1.next = node2
# node2.next = node3
# node2.prev = node1
# node3.next = node4
# node3.prev = node2
# node4.prev = node3
# list1.akhir = node4

# print("Isi Node 1 : ", node1.prev, "-", node1.info, "-", node1.next)
# print("Isi Node 1 : ", node2.prev, "-", node2.info, "-", node2.next)
# print("Isi Node 1 : ", node3.prev, "-", node3.info, "-", node3.next)
# print("Isi Node 1 : ", node4.prev, "-", node4.info, "-", node4.next)


print('--Menu--')
print('1. Tambah Data')
print('2. Hapus Data')
print('3. Tampil Data')
print('0. Keluar')
menu = int(input('Masukan Pilihab Menu : '))

while (menu !=0) :
    if(menu==1) :
        print('Tambah Data')
    elif(menu==2) :
        print('Hapus Data')
    elif(menu==3) :
        list1.TampilData()

    print('--Menu--')
    print('1. Tambah Data')
    print('2. Hapus Data')
    print('3. Tampil Data')
    print('0. Keluar')

while (menu !=0) :
    if(menu==1) :
        print('Tambah Data')
    elif(menu==2) :
        print('Hapus Data')
    elif(menu==3) :
        list1.TampilData()