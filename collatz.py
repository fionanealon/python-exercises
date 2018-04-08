# Fiona Nealon, 2018-03-31
# The Collatz conjecture program

# Create a not equal to 1ariable that will become the answer
n = int(input("Please enter an integer: "))
# Keep looping through numbers that are
while n != 1:
# If n is divisible by 2 without a remainder, divide by 2 and print number
  if (n % 2 == 0):
    n = n/2
    print(int(n))
# If not, multiply n by 3, add 1 and print.
  else:
    n = (3*n)+1
    print(int(n))
