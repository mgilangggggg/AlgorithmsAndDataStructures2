class DataPegawai:
    def __init__(self, pegawai):
        self.info = pegawai
        self.next = None

# Class Untuk Linked List
class LinkedList:
    def __init__(self):
        self.awal = None

    # Fungsi Kosong
    def isEmpty(self):
        return self.awal is None

    # Fungsi Satu Node
    def SatuNode(self):
        bantu = self.awal
        if(bantu.next is None):
            return True
        else:
            return False

    def GajiPokok(self):
        bantu = self.awal
        sementara = []
        while bantu is not None:
            if bantu.info['gol'] == 1:
                gaji = 1000000
            elif bantu.info['gol'] == 2:
                gaji = 2000000
            elif bantu.info['gol'] == 3:
                gaji = 3000000
            elif bantu.info['gol'] == 4:
                gaji = 4000000
            else:
                gaji = 0
                tunjangan = 0
            sementara.append(gaji)
            bantu = bantu.next
        return sementara

    def GajiBersih(self):
        bantu = self.awal
        i = 0
        sementara = []
        while bantu is not None:
            ppn = (point.GajiPokok()[i] + point.Tunjangan()[i]) * 0.05
            hasil = point.GajiPokok()[i] + point.Tunjangan()[i] - ppn
            i += 1
            bantu = bantu.next
            sementara.append(hasil)
        return sementara

    # Fungsi Menentukan Tunjangan Pegawai
    def Tunjangan(self):
        bantu = self.awal
        sementara = []
        while bantu is not None:
            if(bantu.info['gol'] == 1):
                tunjangan = 100000
            elif(bantu.info['gol'] == 2):
                tunjangan = 200000
            elif(bantu.info['gol'] == 3):
                tunjangan = 300000
            elif(bantu.info['gol'] == 4):
                tunjangan = 400000
            else:
                tunjangan = 0
            bantu = bantu.next
            sementara.append(tunjangan)
        return sementara

    # Fungsi Penambahan Data di Depan
    def TambahDataDepan(self, NIP, namaDepan, namaBelakang, gol):
        bantu = self.awal
        ketemu = False
        while(not ketemu) and (bantu is not None):
            if (bantu.info['NIP'] == NIP):
                ketemu = True
            else:
                bantu = bantu.next

        if(ketemu):
            print(f'Data Dengan NIP {NIP} Sudah Terdaftar')
        else:
            sementara = {}
            sementara.update({"NIP": NIP, "namaDepan": namaDepan, "namaBelakang": namaBelakang, "gol": gol})
            Baru = DataPegawai(sementara)
            if (not self.isEmpty()):
                Baru.next = self.awal
            self.awal = Baru
            print('Data Baru Berhasil Ditambahkan')

    # Fungsi Data di Belakang
    def TambahDataBelakang(self, NIP, namaDepan, namaBelakang, gol):
        sementara = {}
        sementara.update({"NIP": NIP, "namaDepan": namaDepan, "namaBelakang": namaBelakang, "gol": gol})
        Baru = DataPegawai(sementara)

        bantu = self.awal
        ketemu = False
        while (not ketemu) and (bantu is not None):
            if (bantu.info['NIP'] == NIP):
                ketemu = True
            else:
                bantu = bantu.next

        if(ketemu):
            print(f'Data Dengan NIP {NIP} Sudah Terdaftar')
        else:
            if (self.isEmpty()):
                self.awal = Baru
            else:
                bantu = self.awal
                while (bantu.next is not None):
                    bantu = bantu.next

                bantu.next = Baru
            print("Data Baru Berhasil Ditambahkan")

    # Fungsi Data di Belakang
    def TambahDataTengah(self, NIP, namaDepan, namaBelakang, gol):
        sementara = {}
        sementara.update({"NIP": NIP, "namaDepan": namaDepan, "namaBelakang": namaBelakang, "gol": gol})
        Baru = DataPegawai(sementara)
        bantuNIP = self.awal
        bantuNama = self.awal
        ketemu = False
        cek = False
        while(not cek) and (bantuNIP is not None):
            if(bantuNIP.info['NIP'] == NIP):
                cek = True
            else:
                bantuNIP = bantuNIP.next

        SisipSetelah = str(input("Masukan Data Setelah  : ")).lower()

        while(not ketemu) and (bantuNama is not None):
            if(bantuNama.info['namaDepan'] == SisipSetelah):
                ketemu = True
            else:
                bantuNama = bantuNama.next

        if(ketemu):
            if(cek):
                print(f"NIP {NIP} Sudah Terdaftar")
            else:
                sementara = {}
                sementara.update({"NIP": NIP, "namaDepan": namaDepan, "namaBelakang": namaBelakang, "gol": gol})
                Baru = DataPegawai(sementara)
                if(bantuNama.next is None):
                    self.TambahDataBelakang(Baru)
                else:
                    Baru.next = bantuNama.next
                    bantuNama.next = Baru
                    print("Data Berhasil Ditambahkan")
        else:
            print("Data ", SisipSetelah, " Tidak Ditemukan")

    # Fungsi Hapus Data di Depan
    def HapusDataDepan(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            Phapus = self.awal
            Element = Phapus.info
            if(self.SatuNode()):
                self.awal = None
            else:
                self.awal = Phapus.next

            del Phapus
            print("Data Yang Dihapus Adalah : ", Element["namaDepan"], Element["namaBelakang"])

    # Fungsi Hapus di Belakang
    def HapusDataBelakang(self):
        if(self is None):
            print("Data Kosong")
        else:
            Phapus = self.awal
            if(self.SatuNode()):
                self.awal = None
            else:
                while(Phapus.next is not None):
                    Phapus = Phapus.next
                    bantu = self.awal

                while(bantu.next is not Phapus):
                    bantu = bantu.next
                bantu.next = None
            Element = Phapus.info

            del Phapus
            print("Data Yang Dihapus Adalah : ", Element["namaDepan"], Element["namaBelakang"])

    # Fungsi Hapus di Tengah
    def HapusDataTengah(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            DataHapus = str(input("Masukan Nama Data Yang Akan Dihapus : "))
            Phapus = self.awal
            ketemu = False
            while(not ketemu) and (Phapus is not None):
                if(Phapus.info["namaDepan"] == DataHapus) or (Phapus.info["namaBelakang"] == DataHapus):
                    ketemu = True
                else:
                    Phapus = Phapus.next

            if(ketemu):
                Element = Phapus.info
                if(Phapus == self.awal):
                    self.HapusDataDepan()
                elif(Phapus.next is None):
                    self.HapusDataBelakang()
                else:
                    bantu = self.awal
                    while(bantu.next is not Phapus):
                        bantu = bantu.next

                    bantu.next = Phapus.next
                    del Phapus
                    print("Data Yang Dihapus Adalah : ", Element["namaDepan"], Element["namaBelakang"])
            else:
                print("Data ", DataHapus, " Tidak Ditemukan")

    # Fungsi Pencarian NIP Tertentu
    def CariNIP(self):
        if(self.isEmpty()):
            print("Data Kosong")
        else:
            NIP = str(input("Masukan NIP Yang Akan Dicari : "))
            bantu = self.awal
            ketemu = False
            while(not ketemu) and (bantu is not None):
                if(bantu.info['NIP'] == NIP):
                    ketemu = True
                else:
                    bantu = bantu.next

            if(ketemu):
                print("NIP        :", bantu.info['NIP'])
                print("Nama       :", bantu.info['namaDepan'], bantu.info['namaBelakang'])
                print("Golongan   :", bantu.info['gol'])
                # print("Gaji       :", bantu.info['gajiPokok'])
                print()
            else:
                print('Data Dengan NIP', NIP,"Tidak Ditemukan")

    # Fungsi Pencarian Nama Tertentu
    def CariNama(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            Nama = str(input("Masukan Nama Yang Akan Dicari : ")).lower()
            bantu = self.awal
            while bantu is not None:
                if(Nama == bantu.info["namaDepan"]) or (Nama == bantu.info["namaBelakang"]) :
                    print(f"Hasil Yang Tersedia Untuk Nama {Nama} :")
                    print("NIP        :", bantu.info['NIP'])
                    print("Nama       :", bantu.info['namaDepan'], bantu.info['namaBelakang'])
                    print("Golongan   :", bantu.info['gol'])
                    print()

                bantu = bantu.next

    # Fungsi Pencarian Golongan Tertentu
    def CariGolongan(self):
        if (self.isEmpty()):
            print("Data Kosong")
        else:
            golongan = int(input("Masukan Gologan Yang Akan Dicari : "))
            bantu = self.awal
            while bantu is not None:
                if(golongan == bantu.info['gol']):
                    print(f"Hasil Yang Tersedia Untuk Golongan {golongan} :")
                    print("NIP        :", bantu.info['NIP'])
                    print("Nama       :", bantu.info['namaDepan'], bantu.info['namaBelakang'])
                    print("Golongan   :", bantu.info['gol'])
                    print()
                else:
                    ketemu = True

                bantu = bantu.next

    # Fungsi Pengubahan Data
    def UbahData(self):
        if(self.isEmpty()) :
            print("Data Kosong")
        else:
            cekData = str(input("Jenis Data Yang Akan di Ubah : ")).lower()
            NIP = str(input("Masukan NIP Data Yang Akan di Ubah : "))
            if(cekData == "1"):
                bantu = self.awal
                ketemu = False
                while(not ketemu) and (bantu is not None):
                    if(bantu.info["NIP"] == NIP):
                        ketemu = True
                    else:
                        bantu = bantu.next

                if(ketemu):
                    namaDepan = str(input("Masukan Nama Depan Baru : "))
                    bantu.info["namaDepan"] = namaDepan
                    namaBelakang = str(input("Masukan Nama Belakang Baru : "))
                    bantu.info["namaBelakang"] = namaBelakang
                    print("Data Berhasil di Ubah")
                else:
                    print(f"Data Dengan NIP {NIP} Tidak Tersedia")

            elif(cekData == "2"):
                bantu = self.awal
                ketemu = False
                while(not ketemu) and (bantu is not None):
                    if(bantu.info["NIP"] == NIP):
                        ketemu = True
                    else:
                        bantu = bantu.next

                if(ketemu):
                    golongan = int(input("Masukan Golongan Baru : "))
                    bantu.info["gol"] = golongan
                    print("Data Berhasil di Ubah")
                else:
                    print(f"Data Dengan NIP {NIP} Tidak Tersedia")

    # Fungsi Untuk Menampilkan Data Setelah Diurut
    def UrutData(self):
        bantu = self.awal
        i = 0
        while (bantu is not None):
            max = bantu
            j = bantu.next
            while (j is not None):
                if (j.info['NIP'] > max.info['NIP']):
                    max = j
                j = j.next

            # Proses Pertukaran
            temp = max.info
            max.info = bantu.info
            bantu.info = temp

            print("NIP         :", bantu.info['NIP'])
            print("Nama        :", bantu.info['namaDepan'], bantu.info['namaBelakang'])
            print("Golongan    :", bantu.info['gol'])
            print("Gaji Pokok  : Rp.", "{:,.2f}".format(point.GajiPokok()[i]))
            print("Tunjangan   : Rp.", "{:,.2f}".format(point.Tunjangan()[i]))
            print("PPN         : 5%")
            print("Gaji Bersih : Rp.", "{:,.2f}".format(round(point.GajiBersih()[i])))
            print()

            # Tempatkan i ke Simpul berikutnya
            i += 1
            bantu = bantu.next

    # Fungsi Untuk Menampilkan Data Sebelum Diurut
    def TampilData(self):
        print('Isi Linked List : ')
        if self.isEmpty() :
            print('Data Kosong')
        else:
            bantu = self.awal
            i = 0
            while bantu is not None:
                print("NIP         :", bantu.info['NIP'])
                print("Nama        :", bantu.info['namaDepan'], bantu.info['namaBelakang'])
                print("Golongan    :", bantu.info['gol'])
                print("Gaji Pokok  : Rp.", "{:,.2f}".format(point.GajiPokok()[i]))
                print("Tunjangan   : Rp.", "{:,.2f}".format(point.Tunjangan()[i]))
                print("PPN         : 5%")
                print("Gaji Bersih : Rp.", "{:,.2f}".format(round(point.GajiBersih()[i])))
                print()
                i += 1
                bantu = bantu.next
            print()

    def BanyakNode(self):
        if self.isEmpty():
            byknode = 0
        else:
            bantu = self.awal
            byknode = 0
            while bantu is not None:
                byknode += 1
                bantu = bantu.next

        return byknode

    def Penghancuran(self):
        Phapus = self.awal
        while Phapus is not None:
            self.awal = Phapus.next
            del Phapus
            Phapus = self.awal

    def MenuPilihan(self):
        print("+-------------------------------------------+\n"
              "|               DAFTAR MENU                 |\n"
              "+-------------------------------------------+\n"
              "| [1] Penambahan Data Pegawai               |\n"
              "| [2] Penghapusan Data Pegawai              |\n"
              "| [3] Pencarian Data Pegawai                |\n"
              "| [4] Pengubahan Data Pegawai (Update Data) |\n"
              "| [5] Tampil Data Pegawai                   |\n"
              "| [0] Keluar                                |\n"
              "+-------------------------------------------+\n")
        Menu = int(input("Masukan Menu : "))
        if(Menu == 1):
            print("\n+-------------------------------------------+\n"
                  "|         MENU PENAMBAHAN DATA              |\n"
                  "+-------------------------------------------+\n"
                  "| [1] Penambahan Data Pegawai Di Depan      |\n"
                  "| [2] Penambahan Data Pegawai Di Belakang   |\n"
                  "| [3] Penambahan Data Pegawai Di Tengah     |\n"
                  "| [0] Keluar                                |\n"
                  "+-------------------------------------------+\n")
            menuTambah = int(input("Masukan Menu Pilihan : "))

            # Input Data
            if(menuTambah == 1) or (menuTambah == 2) or (menuTambah == 3):
                NIP = str(input("Masukan NIP           : "))
                namaDepan = str(input("Masukan Nama Depan    : "))
                namaBelakang = str(input("Masukan Nama Belakang : "))
                gol = int(input("Masukan Golongan      : "))

                if(menuTambah == 1):
                    point.TambahDataDepan(NIP, namaDepan, namaBelakang, gol)
                    point.MenuPilihan()
                elif(menuTambah == 2):
                    point.TambahDataBelakang(NIP, namaDepan, namaBelakang, gol)
                    point.MenuPilihan()
                elif(menuTambah == 3):
                    point.TambahDataTengah(NIP, namaDepan, namaBelakang, gol)
                    point.MenuPilihan()
            else:
                print()
                point.MenuPilihan()


        elif(Menu == 2):
            print("\n+-------------------------------------------+\n"
                  "|         MENU PENGHAPUSAN DATA             |\n"
                  "+-------------------------------------------+\n"
                  "| [1] Penghapusan Data Pegawai Di Depan     |\n"
                  "| [2] Penghapusan Data Pegawai Di Belakang  |\n"
                  "| [3] Penghapusan Data Pegawai Di Tengah    |\n"
                  "| [0] Keluar                                |\n"
                  "+-------------------------------------------+\n")
            menuHapus = int(input("Masukan Menu Pilihan : "))
            if(menuHapus == 1):
                point.HapusDataDepan()
                point.MenuPilihan()
            elif(menuHapus == 2):
                point.HapusDataBelakang()
                point.MenuPilihan()
            elif(menuHapus == 3):
                point.HapusDataTengah()
                point.MenuPilihan()
        elif(Menu == 3):
            print("\n+-------------------------------------------+\n"
                  "|            MENU PENCARIAN DATA            |\n"
                  "+-------------------------------------------+\n"
                  "| [1] Pencarian NIP                         |\n"
                  "| [2] Pencarian Nama                        |\n"
                  "| [3] Pencarian Golongan                    |\n"
                  "| [0] Keluar                                |\n"
                  "+-------------------------------------------+\n")
            menuCari = int(input("Masukan Menu Pilihan : "))
            if (menuCari == 1):
                point.CariNIP()
                point.MenuPilihan()
            elif (menuCari == 2):
                point.CariNama()
                point.MenuPilihan()
            elif (menuCari):
                point.CariGolongan()
                point.MenuPilihan()
        elif(Menu == 4):
            print("\n+-------------------------------------------+\n"
                  "|           DATA YANG BISA DIUBAH           |\n"
                  "+-------------------------------------------+\n"
                  "| [1] Nama                                  |\n"
                  "| [2] Golongan                              |\n"
                  "+-------------------------------------------+\n")
            point.UbahData()
            point.MenuPilihan()
        elif(Menu == 5):
            print("Data Sebelum Diurut")
            point.TampilData()
            print("Data Sesudah Diurut")
            point.UrutData()
            point.MenuPilihan()



point = LinkedList()

node1 = DataPegawai({"NIP": "10121167", "namaDepan": 'ahmad', "namaBelakang": 'jaenal', "gol": 4})
node2 = DataPegawai({"NIP": "10121177", "namaDepan": 'muhammad', "namaBelakang": 'gilang', "gol": 1})
node3 = DataPegawai({"NIP": "10121200", "namaDepan": 'noval', "namaBelakang": 'aulia', "gol": 2})
node4 = DataPegawai({"NIP": "10121185", "namaDepan": 'muhammad', "namaBelakang": 'fitrian', "gol": 3})

point.awal = node1
node1.next = node2
node2.next = node3
node3.next = node4

point.MenuPilihan()
point.Penghancuran()
point.TampilData()
