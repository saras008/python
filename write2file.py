import os
import csv

def create_file(filename):
    with open(filename,'w') as file:
        file.write("name,color,type\n")
        file.write("carnation,pink,annual\n")
        file.write("daffodil,yellow,parennial\n")

def parsingtocsv(filename):
    return_string= ""
    with open(filename,'r') as file:
        convert = csv.DictReader(file)
        print(convert)
        for row in convert:
            print(row)   
    #         return_string += "a {} {} is {}\n".format(row["color"],row["name"],row["type"])
    # return return_string

create_file("cobanulis.txt")
parsingtocsv("cobanulis.txt")