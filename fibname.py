# Fiona Nealon

# A program that displays Fibonacci numbers using people's names.



def fib(n):

  """This function returns the nth Fibonacci number."""
# Creates variables that will become the answer
  i = 0

  j = 1

  n = n - 1


# Keeps looping through numbers that are greater than 0
  while n >= 0:
# Varaiable on right '=' are calculated first, then assigned to left of '='
    i, j = j, i + j
# Acts as a counter for loop, each loop n is de-incremented by 1
    n = n - 1

  
# When loop ends, return i
  return i


# Creates the string
name = "Nealon"
# Finds first element of string
first = name[0]
# Finds last element of string
last = name[-1]
# Converts ASCII char to dec
firstno = ord(first)
# Converts ASCII char to dec
lastno = ord(last)
# Add to assign value of x
x = firstno + lastno



ans = fib(x)
# Tests from question
print("My surname is", name)

print("The first letter", first, "is number", firstno)

print("The last letter", last, "is number", lastno)

print("Fibonacci number", x, "is", ans)
