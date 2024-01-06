class LinearQueue :
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
        if (self.rear == self.maxAngka-1) :
            return True
        else :
            return False

    def Enqueue(self, DataBaru) :
        if (not self.Penuh()) :
            if (self.Kosong()) :
                self.front = 0
                self.rear = 0
            else :
                self.rear += 1
            self.data.append(DataBaru)
        else :
            print('Queue Angka Penuh')

    def Dequeue(self) :
        if (not self.Kosong()) :
            item = self.data[self.front]
            for i in range(0,self.rear-1) :
                self.data[i] = self.data[i+1]
            self.rear -= 1
            print('Data Yang Keluar : ',item)
        else :
            print('Queue Angka Kosong')

        
    def TampilData(self) :
        out = 'Queue Array (['
        if (not self.Kosong()) :
            for i in range (0, self.rear) :
                out = out + str(self.data[i]) + " "
        else :
            out = out + "Queue Angka Kosong"
        out = out + "]"
        out = out + ")"
        print(out)

q = LinearQueue(maxAngka=3)

q.TampilData()
q.Enqueue(1)
q.TampilData()
DataBaru = int(input('Masukan Data Angka 1 : '))
q.Enqueue(DataBaru)
DataBaru = int(input('Masukan Data Angka 2 : '))
q.Enqueue(DataBaru)
DataBaru = int(input('Masukan Data Angka 3 : '))
q.Enqueue(DataBaru)
q.Dequeue()
q.TampilData()