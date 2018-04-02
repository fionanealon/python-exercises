# Exerise 1

Please complete the following exercise this week. In the video lectures this week we ran an example program that calculated the 30th Fibonacci number. Change the program to calculate the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers. Take A as the number 1, B as 2, C as 3, and so on. For example, my name is Ian, so I should calculate the 25th Fibonacci number because I is 9 and n is 14, giving 25 in total. Once you calculate the right Fibonacci number for your own name, please post it to the Discussions forum on this page as per my post there.

## References

Wikipedia contributors. "Fibonacci Number." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 28 Mar. 2018. Web. 28 Mar. 2018.< https://en.wikipedia.org/wiki/Fibonacci_number
Python Software Foundation. The Python Tutorial, Python 3.6.5 documentation. Available at https://docs.python.org/3/tutorial/
Python Software Foundation. Python Language Reference, version 2.7. Available at http://www.python.org

## Answer to Exercise 1

My name is Fiona, so the first and last letter of my name (F + A = 6 + 1) give the number 7. The 7th Fibonacci number is 13. 
![A picture of forum](Forum.JPG)

## Python code used to run this program

Adapted from https://github.com/ianmcloughlin/python-fib/blob/master/fib.py

- Ian McLoughlin

- A program that displays Fibonacci numbers.

def fib(n):

  """This function returns the nth Fibonacci number."""

  i = 0

  j = 1

  n = n - 1



  while n >= 0:

    i, j = j, i + j

    n = n - 1

  

  return i



# Test the function with the following value.

x = 7

ans = fib(x)

print("Fibonacci number", x, "is", ans)

## How to run this code
1. Download Anaconda
2. Install Anaconda
