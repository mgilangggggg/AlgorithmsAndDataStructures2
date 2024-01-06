class CircularQueue :
    def __init__(self, maxAngka):
        self.data = []
        self.front = -1
        self.rear = -1
        self.maxAngka = maxAngka

    def Kosong(self) :
        if (self.rear == -1) :
            return True
        else :
            return False

    def Penuh(self) :
        if (self.front == 1 and self.rear == self.maxAngka) or (self.rear == self.front-1) :
            return True
        else :
            return False

    def Enqueue(self, DataBaru) :
        if (not self.Penuh()) :
            if (self.Kosong()) :
                self.front = 0
                self.rear = 0
            elif (self.rear == self.maxAngka-1) :
                self.rear = 0
            else :
                self.rear += 1
            self.data.append(DataBaru)
        else :
            print('Queue Angka Penuh')

    def Dequeue(self) :
        if (not self.Kosong()) :
            item = self.data[self.front]
            
            if (self.front == self.maxAngka) :
                self.front = 0
            elif (self.front == self.rear) :
                self.front = 0
                self.rear = 0
            else :
                self.front = 0

            print('Data Yang Keluar : ',item)
        else :
            print('Queue Angka Kosong')

        
    def TampilData(self) :
        '''out = 'Queue Array (['
        if (not self.Kosong()) :
            if (self.rear < self.front) :
                for i in range (0,self.rear) :
                    out = out +str(self.data[i]) + " "
                for i in range (self.front, self.maxAngka) :
                    out = out + str(self.data[i]) + " "
            else :
                for i in range (self.front, self.rear+1) :
                    out = out +str(self.data[i]) + " "
        else :
            out = out + "Queue Angka Kosong"
        out = out + "]"
        out = out + ")"
        print(out)'''
        print('MENU PILIHAN')
        print('============')
        print('1. Tambah Data Ke Queue Angka')
        print('2. Keluarkan Data Dari Queue Angka')
        print('0. Keluar')
        print(self.data)
        print('Front : ',self.front)
        print('Rear  : ',self.rear)

q = CircularQueue(maxAngka=3)

q.TampilData()
q.TampilData()
DataBaru = int(input('Masukan Data Angka 1 : '))
q.Enqueue(DataBaru)
DataBaru = int(input('Masukan Data Angka 2 : '))
q.Enqueue(DataBaru)
DataBaru = int(input('Masukan Data Angka 3 : '))
q.Enqueue(DataBaru)
q.TampilData()
q.Dequeue()
q.TampilData()
DataBaru = int(input('Masukan Data Angka 4 : '))
q.Enqueue(DataBaru)
q.TampilData()
# q.Dequeue()
# q.TampilData()
DataBaru = int(input('Masukan Data Angka 5 : '))
q.Enqueue(DataBaru)
q.TampilData()