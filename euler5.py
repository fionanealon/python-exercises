# Fiona Neealon, 04-05-2018
# "The smallest positive number that is evenly divisible by all of the numbers from 1 to 20"


def factorial(upto):
  multupto = 1
  for i in range (1, upto):
    if multupto % i > 0: 
        for k in range (1, upto):
            if (multupto * k) % i == 0: 
                multupto = multupto * k
                break
  return multupto

print("The smallest positive number that is evenly divisible by all of the numbers from 1 to 20", factorial(4)) 
  

