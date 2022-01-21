from reader import Reader
import sys
import csv

# read a csv file
reader = Reader()

if (len(sys.argv) > 1):
    reader.setFilename(sys.argv[1])

data_list = reader.getData()

# debug: print csv data into terminal
print(data_list)

# Print thetas into csv
headers = ['theta0', 'theta1']
thetas = ['-0.02145', '8499.5996'] # will be estimated by linear regression

with open('theta.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerow(thetas)
