import csv
import numpy as np
import sys


class Reader:

    def __init__(self, filename="data.csv"):
        self.filename = filename

    def getData(self):
        try:
            data = np.genfromtxt(self.filename, delimiter=',',
                                 skip_header=0, dtype=None, encoding='utf8')
            
            if (data.shape[0] < 3 or len(data.shape) < 2):
                sys.exit(f"Invalid file: {self.filename}")

            headers = data[0]
            x = data[1:, 0].astype(np.float64)
            y = data[1:, 1].astype(np.float64)
            x = x.reshape(x.shape[0], 1)
            y = y.reshape(y.shape[0], 1)

        except IOError:
            print(f"Could not read file: {self.filename}")
            sys.exit(1)
        return headers, x, y

    def getTheta(self):
        try:
            with open(self.filename, newline='') as data_file:
                reader = csv.reader(data_file)
                theta = list(reader)
            if (len(theta) < 2):
                sys.exit(f"Invalid file: {self.filename}")
            if (len(theta[1]) < 2):
                sys.exit(f"Invalid file: {self.filename}")            

        except IOError:
            print(f"Could not read file: {self.filename}")
            return 0., 0.
        return float(theta[1][1]), float(theta[1][0])

    def setFilename(self, filename):
        print(f"File read: {filename}")
        self.filename = filename

# def getData(self):
#     try:
#         with open(self.filename, newline='') as data_file:
#             reader = csv.reader(data_file)
#             self.data_list = list(reader)
#            # for row in reader:
#            #     self.data_list.append(row)
#         # self.data_list.pop(0)
#     except IOError:
#         print(f"Could not read file: {self.filename}")
#         sys.exit(1)
#     return self.data_list

# def getHeaders(self):
#     return self.data_list[0]

# def getColums(self):
#     try:
#         with open(self.filename, newline='') as data_file:
#             file = csv.DictReader(data_file)
#             for col in file:
#                 self.mileage.append(int(col['km']))
#                 self.price.append(int(col['price']))
#     except IOError:
#         print(f"Could not read file: {self.filename}")
#         sys.exit(1)
#     return self.mileage, self.price

# def sortData(self):
#     # self.data_list = sorted(self.data_list, key=lambda x:int(x[0]))
#     for lst in self.data_list:
#         self.mileage.append(int(lst[0]))
#         self.price.append(int(lst[1]))
#     return self.mileage, self.price
