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
print(data_list)

# convert thetas from string to float
theta0 = float(data_list[1][0])
theta1 = float(data_list[1][1])
print(f'theta0: {theta0}')
print(f'theta1: {theta1}')

# retrieve the mileage given in arg
if (len(sys.argv) > 1):
    mileage =  float(sys.argv[1])
else:
    sys.exit("Need a mileage to run the estimation")

# test the mileage
max_mileage = theta1 / (theta0 * -1)
if (mileage < 0):
    sys.exit("The mileage needs to be a positive value")
# elif (mileage > max_mileage):
#     sys.exit(f"The mileage can't be > than {max_mileage:.0f} km")
print(f'Mileage given: km {mileage:15,.2f}')

# calculate the price with mileage
if (mileage > max_mileage):
    price = 0
else:
    price = theta0 * mileage + theta1
print(f'Estimted price: $ {price:15,.2f}')