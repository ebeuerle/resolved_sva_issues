import csv

class CsvWriter(object):

    @staticmethod
    def write(output):
        with open("output.csv", "wb") as f:
            writer = csv.writer(f)
            writer.writerows(output)