def fibo(N) :
    if N == 0:
        return (N)
    angka = fibo(N-1)
    index = len(angka)

    angka1 = index(-2) if index > 2 else 0
    angka2 = index(-1) if index > 2 else 1

    return numbers + (angka1 + angka2)

tampil = int(input("Masukan Angka : "))

print(fibo(angka-1))