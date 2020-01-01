import csv
import matrix_gen as mx

def s(d):
    print(d)


with open(mx.filename) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        # print(row)
        pass

s("ss")