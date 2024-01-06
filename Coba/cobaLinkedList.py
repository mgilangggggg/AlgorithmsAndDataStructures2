# Pendefinisian

# Class Node
class Data :
    def __init__(self, info) :
        self.info = info
        self.next = None

# Class Motor
class merkMotor :
    def __init__(self) :
        self.awal = None
    
    def isEmpty(self) :
        return self.awal is None

    def TampilData(self) :
        print('Isi Data : ',end='')
        if self.isEmpty() :
            print('Data Kosong')
        else :
            bantu = self.awal
            while bantu is not None :
                print(bantu.info,'',end='')
                if bantu.next is not None :
                    print('->',end=' ')
                bantu = bantu.next
            print()      

    def BanyakData(self) :
        if self.isEmpty() :
            banyakData = 0
        else :
            bantu = self.awal
            banyakData = 0
            while bantu is not None :
                banyakData = banyakData + 1
                bantu = bantu.next
            return banyakData

    def TambahPertama(self, DataBaru) :
        baru = Data(DataBaru)
        if (not self.isEmpty()) :
            baru.next = self.awal
            self.awal = baru

    def Penghancuran(self) :
        Phapus = self.awal
        while Phapus is not None :
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

# inisialisasi
list1 = merkMotor()
print('Awal : ',list1.awal)

# memasukan data ke motor
data1 = Data('Honda')
data2 = Data('Yamaha')
data3 = Data('suzuki')
data4 = Data('KTM')

print('Isi Data 1 :',data1.info,'=', data1.next)
print('Isi Data 2 :',data2.info,'=',data2.next)
print('Isi Data 3 :',data3.info,'=',data3.next)
print('Isi Data 4 :',data4.info,'=',data4.next)

# Membuat linked list
list1.awal = data1
data1.next = data2
data2.next = data3
data3.next = data4

print('Isi Data 1 :',data1.info,'=', data1.next)
print('Isi Data 2 :',data2.info,'=',data2.next)
print('Isi Data 3 :',data3.info,'=',data3.next)
print('Isi Data 4 :',data4.info,'=',data4.next)

# traversal menampilkan data
list1.TampilData()

# traversal Menghitung banyak data
print('Banyak Data Motor : ' ,list1.BanyakData())

# Tampil Data baru pertama
DataBaru = int(input('Masukan Data Baru : '))

# Penghancuran
list1.Penghancuran()
list1.TampilData()
print('Banyak Data Motor : ' ,list1.BanyakData())
