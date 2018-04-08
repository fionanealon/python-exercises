# Fiona Nealon, 2018-04-07
# A function called factorial() which takes a single input and returns it's factorial


def factorial(upto):
# Create a variable that will become the answer
  multupto = 1
# Loop through numbers i from 1 to upto
  for i in range(1, upto + 1):
# Multiply ans by i, changing ans to that
    multupto = multupto * i
# Return the factorial    
  return multupto
# Tests from questions
print("The multiplication of the values from to 1 to 5 inclusive is", factorial(5))
print("The multiplication of the values from to 1 to 7 inclusive is", factorial(7))
print("The multiplication of the values from to 1 to 10 inclusive is", factorial(10)) 
