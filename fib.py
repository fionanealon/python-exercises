# Fiona Nealon
# A program that displays Fibonacci numbers.



def fib(n):

  """This function returns the nth Fibonacci number."""
# Creates variables that will become the answer
  i = 0

  j = 1

  n = n - 1


# Keeps looping through numbers that are greater than 0
  while n >= 0:
# Variables on right  of'=' are calculated first, then assigned to left of '='
    i, j = j, i + j
# Acts as a counter for loop, each loop n is de-incremented by 1
    n = n - 1

  
# When loop ends, return i
  return i



# Assisgns a value to x

x = 7


ans = fib(x)

print("Fibonacci number", x, "is", ans)
