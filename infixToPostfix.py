# Program Konversi Notasi Infix ke Postfix
# I.S. : Pengguna Memasukan Notasi Infix
# F.S : Program Menampilkan Bentuk Notasi Postfix dan Hasil Perhitungan

Operator = set(['+','-','*','/','(',')','^']) #kumpulan operator
Prioritas = {'+':1,'-':1,'*':2,'/':2,'^':3} #Prioritas Operator

def konversi(ekspresi) :
    stack = [] #inisialisasi stack kosong
    output = []

    for karakter in ekspresi : 
        # print(karakter)
        if (karakter not in Operator) :
            output.append(karakter)
        elif (karakter=='(') :
            stack.append('(')
        elif (karakter ==')') :
            while stack and stack[-1] != "(" :
                output.append(stack.pop())
            stack.pop()
        else :
            while stack and stack[-1] != "(" and Prioritas[stack[-1]] >= Prioritas[karakter] :
                output.append(stack.pop())
                print(output)
            stack.append(karakter)

# Menampilakan setiap perulangan
        # print(output)
        # print(stack)
        # print()

    while stack :
        output.append(stack.pop())
    return output

def PerhitunganPostfix(ekspresi) :
    stack = []
    output = ''

    for karakter in ekspresi :
        if (karakter not in Operator) :
            stack.append(karakter)
        else :
            A = int(stack.pop())
            B = int(stack.pop())

            if (karakter == '+') :
                hasil = B + A
            elif (karakter == '-') :
                hasil = B - A
            elif (karakter == '*') :
                hasil = B * A
            elif (karakter == '/') :
                hasil = B / A
            elif (karakter == '^') :
                hasil = B ** A
            
            stack.append(hasil)

    while stack :
        output = stack.pop()
    return output
    
def Tampil(ekspresi) :
    output = ''
    for karakter in ekspresi :
        output += karakter
    return output

print ('--Program Konversi Infix to Postfix--')
ekspresi = input('Notasi Infix : ')
NotasiInfix = konversi(ekspresi.split())
print('Bentuk Notasi Postfix : ',Tampil(NotasiInfix))
print('Hasil Perhitungan : ',PerhitunganPostfix(NotasiInfix))