from reader import Reader
import sys
import csv

mileage = 0
price = 0
theta0 = 0
theta1 = 0
max_mileage = 0

# read the theta csv file
reader = Reader()
reader.setFilename("theta.csv")
data_list = reader.getData()
# print(data_list)

# convert thetas from string to float
theta0 = float(data_list[1][1])
theta1 = float(data_list[1][0])
# print(f'theta0: {theta0}')
# print(f'theta1: {theta1}')

# retrieve the mileage given in input
mileage = input("Enter the mileage of the car (km): ")

if (mileage.isdigit()):
    mileage = int(mileage)
else:
    sys.exit("The mileage needs to be a integer value")

# test the mileage
if (mileage < 0):
    sys.exit("The mileage needs to be a positive value")

# calculate the price with mileage
if (theta1 == 0. or theta0 <= 0):
    max_mileage = -1
else:
    max_mileage = theta0 / (theta1 * -1)

if (mileage < max_mileage):
    price = theta1 * mileage + theta0

print(f'Estimted price ($): {price:.0f}')