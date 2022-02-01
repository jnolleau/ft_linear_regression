from csvReader import Reader
import sys

mileage = 0
price = 0
theta0 = 0
theta1 = 0
max_mileage = 0

# read the theta csv file
rd = Reader()
rd.setFilename("theta.csv")
theta0, theta1, max = rd.getTheta()

# retrieve the mileage given in input
mileage = input("Enter the mileage of the car (km): ")

# test the mileage
if (mileage.isdigit()):
    mileage = int(mileage)
else:
    sys.exit("The mileage needs to be a positive integer value")

if (mileage < 0):
    sys.exit("The mileage needs to be a positive value")

# calculate the price with mileage
if (theta1 == 0.):
    max_mileage = -1
else:
    max_mileage = theta0 / (theta1 / max * -1)

if (mileage < max_mileage):
    price = theta0 + theta1 * mileage / max

print(f'Estimted price ($): {price:.0f}')
