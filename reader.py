import csv
import sys


class Reader:

    def __init__(self, filename="data.csv"):
        self.filename = filename
        self.data_list = []

    def getData(self):
        try:
            with open(self.filename, newline='') as data_file:
                reader = csv.reader(data_file)
                for row in reader:
                    self.data_list.append(row)

        except IOError:
            print(f"Could not read file: {self.filename}")
            sys.exit(1)
        return self.data_list

    def setFilename(self, filename):
        print(f"File read: {filename}")
        self.filename = filename
