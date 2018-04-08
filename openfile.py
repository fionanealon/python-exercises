# Fiona Nealon, 2018-04-05
# A program that reads and formats the Iris Data set

# Open the data csv file in data sub folder. Also close the data csv file once complete. 
with open("data/iris.csv")as f:
# Loop through lines of data csv file 
  for line in f:
# Tests from question
    print(line.split(',')[0], line.split(',')[1], line.split(',')[2], line.split(',')[3])

  