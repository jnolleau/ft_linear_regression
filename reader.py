import csv
import sys


class Reader:

    def __init__(self, filename="data.csv"):
        self.filename = filename
        self.data_list = []
        # self.mileage = []
        # self.price = []

    def getData(self):
        try:
            with open(self.filename, newline='') as data_file:
                reader = csv.reader(data_file)
                self.data_list = list(reader)
               # for row in reader:
               #     self.data_list.append(row)
            # self.data_list.pop(0)
        except IOError:
            print(f"Could not read file: {self.filename}")
            sys.exit(1)
        return self.data_list

    def getHeaders(self):
        return self.data_list[0]

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

    def setFilename(self, filename):
        print(f"File read: {filename}")
        self.filename = filename
