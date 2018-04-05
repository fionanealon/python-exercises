# Fiona Nealon, 2018-04-05
# A program that reads and formats the Iris Data set

with open("data/iris.csv")as f:
  for line in f:
    print(line.split(',')[0])
  