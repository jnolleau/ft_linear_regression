from reader import Reader
import sys
import csv

reader = Reader()

if (len(sys.argv) > 1):
    reader.setFilename(sys.argv[1])

data_list = reader.getData()

print(data_list)

thetas = ['42.42', '21.21']

with open('tetha.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(thetas)

# with open("tetha.csv", 'w') as tehtas_file:
#     tehtas_file.write("theta0,theta1\n")
#     tehtas_file.writelines(thetas)

