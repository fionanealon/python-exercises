# Fiona Nealon, 2018-03-31
# The Collatz conjecture program

n = int(input("Please enter an integer: "))

while n != 1:
  if (n % 2 == 0):
    n = n/2
    print(int(n))
  else:
    n = (3*n)+1
    print(int(n))
