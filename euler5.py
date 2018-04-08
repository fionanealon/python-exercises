# Fiona Neealon, 2018-04-2018
# A program that finds the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

def factorial(upto):
# Create a variable that will become the answer
  multupto = 1
# Loop through numbers i from 1 to upto
  for i in range (1, upto):
# # Adapted from: https://stackoverflow.com/questions/8024911/project-euler-5-in-python-how-can-i-optimize-my-solution
# If the number is not divisible by i
    if multupto % i > 0: 
# Loop through numbers k from 1 to upto
        for k in range (1, upto):
# Find the smallest number divisible by i   
            if (multupto * k) % i == 0:
# Multiply ans by k, changing ans to that
                multupto = multupto * k
                break
  return multupto

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20", factorial(20)) 
  

