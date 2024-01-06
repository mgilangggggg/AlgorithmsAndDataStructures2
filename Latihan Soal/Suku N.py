
N = int(input("Masukan  Nilai N : "))

def fibonacci (N):
  if (N == 0) or (N == 1):
    return N
  else:
    return fibonacci(N - 2) + fibonacci(N - 1)

print ("Suku ke", N , "dari Fibonacci adalah ", fibonacci(N))