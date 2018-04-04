# Exercise 1
Please complete the following exercise this week. In the video lectures this week we ran an example program that calculated the 30th Fibonacci number. Change the program to calculate the nth Fibonacci number where n the sum of the first and last letters of your first name as numbers. Take A as the number 1, B as 2, C as 3, and so on. For example, my name is Ian, so I should calculate the 25th Fibonacci number because I is 9 and n is 14, giving 25 in total. Once you calculate the right Fibonacci number for your own name, please post it to the Discussions forum on this page as per my post there.

## References
Wikipedia contributors. "Fibonacci Number." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 28 Mar. 2018. Web. 28 Mar. 2018.< https://en.wikipedia.org/wiki/Fibonacci_number

IPython Software Foundation. The Python Tutorial, Python 3.6.5 documentation. Available at https://docs.python.org/3/tutorial/

Python Software Foundation. Python Language Reference, version 2.7. Available at http://www.python.org

## Answer to Exercise 1
My name is Fiona, so the first and last letter of my name (F + A = 6 + 1) give the number 7. The 7th Fibonacci number is 13. 
![A picture of forum](Forum.JPG)

## Introduction
A Fibonacci number sequence is a sequence of numbers where the first two Fibonacci numbers are 0 and 1. The next Fibonacci number is the sum of the previous 2 Fibonacci numbers. 
The 7th Fibonacci number in the Fibonacci number sequence = 13 (0 1 1 2 3 5 8 13)

## Analysis and discussion of Exercise 1

The function fib calculates the 7th Fibonacci number using a while loop. 

A while loop in python programming repeatedly executes a target statement as long as a given condition is true. In this case, the while loop repeatedly executes a multiple assignment statement as long as n > 0.

In the multiple assignment, all values on the right side of the ‘=‘are calculated first and then assigned to the variables on the left side of the ‘=‘. For example, the first time through the loop the values for i and j are as follows:
```python
i = 0
j = 1
```
When they reach the multiple assignment, you can substitute these values for the variables and see the new values for i and j:
```python
i, j = 1, 0 + 1
```
So now:
```python
i = 1
j = 1
```
In the next iteration of the loop (2):
```python
i, j = 1, 1 + 1
```
so now: 
```python
i = 1
j = 2
```
In the next iteration of the loop (3):
```python
i, j = 2, 1 + 2
```
so now: 
```python
i = 2
j = 3
```
In the next iteration of the loop (4):
```python
i, j = 3, 2 + 3
```
so now: 
```python
i = 3
j = 5
```
In the next iteration of the loop (5):
```python
i, j = 5, 3 + 5
```
so now: 
```python
i = 5
j = 8
```
In the next iteration of the loop (6):
```python
i, j = 8, 5 + 8
```
so now: 
```python
i = 8
j = 13
```
In the next iteration of the loop (7):
```python
i, j = 13, 8 + 13
```
so now: 
```python
i = 13
j = 21
```
The most important variable is i as it is the one that is returned at the end of the function. You can see that the 7 times that we’ve gone through the loop the value of i has been set to a number from the sequence:

0, 1, 1, 2, 3, 5, 8, 13

In the while loop the reason that you have n = n - 1  is to act as a counter. Every time we go through the loop n is de-incremented by 1 so if n = 7 the first time through the loop it becomes 6 the next time through and so on until it becomes -1 which then fails the condition of the while loop (n >= 0) and the while loop ends.

After the while loop ends, the next line is the last of the function:
```python
return i
```
This line returns the last value of i which was generated in the while loop.

Everything up to this point has been discussing the contents of the function fib.

The next part is not part of the function:
```python
x = 7
ans = fib(x)
print("Fibonacci number", x, "is", ans)
```

So…
x = 7 assigns the value of 7 to x.
```python
ans = fib(x)
```
Since x = 7, this can be written:
```python
ans = fib(7)
```
What this line is doing is calling the function fib with an argument of 7 and we look at the definition of fib, def fib(n):, what you can see is that the initial n value of the function is being set to 7. What happens now is that the function does it’s work, looping 7 times and setting the value of i each time through the loop and when the loop is finished it returns the value of i. it is this value that is assigned to ans.
The last line:
```python
print("Fibonacci number", x, "is", ans)
```

This prints:

"Fibonacci number”, then the value of x, then “is” and then the value of ans.
In this case, since x is 7 then it prints:

Fibonacci number 7 is 13

## How to run this code:

1. Download [Anaconda](https://anaconda.org/).
2. Install Anaconda
3. Download [Visual Studio Code](https://code.visualstudio.com/download).
4. Install Visual Studio Code
5. Save a new folder on desktop e.g. Python Scripts
6. Save fib.py file into this folder
7. Open Visual Studio Code
8. Open Python Scripts folder from desktop
9. Open fib.py file
10.	Open integrated terminal in Visual Studio code
11. Type ‘python fib.py’ in the command prompt 
12.	Press enter

## Result:



## Exercise 2

https://github.com/ianmcloughlin/python-fib/blob/master/fibname.py

Above is a link to a program I wrote that works similarly to last week's exercise. Copy and run the program yourself. Change the string variable to contain your own surname, and rerun it. Can you figure out what ord() does? Try to Google it to find out. Post the output of the program, along with any insight you have as to what ord() does, to the discussions forum.

## References

Wikipedia contributors. "Fibonacci Number." Wikipedia, The Free Encyclopedia. Wikipedia, The Free Encyclopedia, 28 Mar. 2018. Web. 28 Mar. 2018.< https://en.wikipedia.org/wiki/Fibonacci_number

IPython Software Foundation. The Python Tutorial, Python 3.6.5 documentation. Available at https://docs.python.org/3/tutorial/

Python Software Foundation. Python Language Reference, version 2.7. Available at http://www.python.org

## Answer to Exercise 2

My surname is Nealon

The first letter N is number 78

The last letter n is number 110

Fibonacci number 188 is 871347450517368352816615810882615488381

The ord() method converts the characters into their corresponding ASCII value.


## Introduction

This program displays Fibonacci numbers using people's names. A Fibonacci number sequence is a sequence of numbers where the first two Fibonacci numbers are 0 and 1. The next Fibonacci number is the sum of the previous 2 Fibonacci numbers. The sequence continues until the required Fibonaaci number is reached.


## Analysis and discussion of Exercise 2

This program is similar to the program in Exercise 1. In this program, the while loop also repeatedly executes a multiple assignment statement as long as n > 0.

To find the value n:
```python
name = "Nealon"
first = name[0]
last = name[-1]
firstno = ord(first)
lastno = ord(last)
x = firstno + lastno
```
This program finds the first letter and the last letter of the name "Nealon" - "N and "n". The ord() function then converts the 'N' and 'n'  ASCII characters into decimal values so "N"=78 and "n"=110. On the next line, 78 and 110 are then added together to assign the value of x.
```python
ans = fib(x)
```
Since x = 188, this can be written:
```python
ans = fib(188)
```
This line is doing is calling the function fib with an argument of 188 and if we look at the definition of fib, def fib(n):, what you can see is that the initial n value of the function is being set to 188. What happens now is that the function does it’s work, looping 188 times and setting the value of i each time through the loop and when the loop is finished it returns the value of i. 

To explain def fib(n): In the multiple assignment of the while loop, all values on the right side of the ‘=‘are calculated first and then assigned to the variables on the left side of the ‘=‘. For example, the first time through the loop the values for i and j are as follows:
```python
i = 0
j = 1
```
When they reach the multiple assignment, you can substitute these values for the variables and see the new values for i and j:
```python
i, j = 1, 0 + 1
```
So now:
```python
i = 1
j = 1
```
In the next iteration of the loop (2):
```python
i, j = 1, 1 + 1
```
so now: 
```python
i = 1
j = 2
```
In the next iteration of the loop (3):
```python
i, j = 2, 1 + 2
```
so now: 
```python
i = 2
j = 3
```
This continues until the 188th iteration of the loop after which n becomes -1 which then fails the condition of the while loop (n >= 0) and the while loop ends. n = n - 1  is to act as a counter for this iteration.
```python
i, j = 871347450517368352816615810882615488381, 538522340430300790495419781092981030533 + 871347450517368352816615810882615488381
```
so now: 
```python
i = 871347450517368352816615810882615488381
j = 1409869790947669143312035591975596518914
```
After the while loop ends, the next line is the last of the function:
```python
return i
```
This line returns the last value of i which was generated in the while loop.

The last line:
```python
ans = fib(x)
print("My surname is", name)
print("The first letter", first, "is number", firstno)
print("The last letter", last, "is number", lastno)
print("Fibonacci number", x, "is", ans)
```
This prints:
1. "My surname is”, then the name (line 16 of the program) on the first sentence at the command prompt. 

In this case, since name is Nealon then it prints:

My surname is Nealon
2. "The first letter", then then the value of first (line 17 of the program,) then "is number", then the value of firstno (line 19 of the program) on the second sentence at the command prompt. 

In this case, since first is N and firstno is 78 it prints:

The first letter N is number 78
3. "The last letter", then then the value of last (line 18 of the program,) then "is number", then the value of lastno (line 20 of the program) on the third sentence at the command prompt. 

In this case, since last is n and firstno is 110 it prints:

The last letter n is number 110
4. "Fibonacci number”, then the value of x, then “is” and then the value of ans.

In this case, since x is 188 then it prints:

Fibonacci number 188 is 871347450517368352816615810882615488381

How to run this code:

    Download Anaconda
    Install Anaconda
    Download Visual Studio Code
    Install Visual Studio Code
    Save a new folder on desktop e.g. Python Scripts

     Save fib.py file into this folder

    Open Visual Studio Code
    Open Python Scripts folder from desktop
    Open fib.py file

    Open integrated terminal in Visual Studio code

    Type ‘python fib.py’ in the command prompt

    Press enter

Result:

Picture



