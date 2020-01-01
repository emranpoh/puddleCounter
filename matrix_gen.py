import random, csv, sys

verbose = False

type_sym = ["░░","▒▒","▓▓"]

w = int(input("Enter width : "))
h = int(input("Enter height : "))

if(verbose): print("Width: ",end="")
if(w == ""):
    if(verbose): print("10 (DEF)",end="")
    w = 10
else:
    if(verbose): print(w,end="")

if(verbose): print(" Height: ",end="")
if(h == ""):
    if(verbose): print("10 (DEF)",end="")
    h = 10
else:
    if(verbose): print(h,end="")
if(verbose): print()

types = 2

matrix = [[0 for x in range(w)] for y in range(h)] 

for y in range(0,h):
    for x in range(0,w):
        matrix[y][x] = random.randint(0,types-1)

for i in matrix:
    for j in i:
        if(verbose): print(type_sym[j],end="")
    if(verbose): print("")

filename = "w" + str(w) + "_h" + str(h) + ".csv"

with open(filename, mode='w') as employee_file:
    w = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for i in matrix:
        w.writerow(i)

    print("Generated " + filename)