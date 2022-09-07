import csv

infile = open('customers.csv','r')

csvfile = csv.reader(infile,delimiter=',')

next(csvfile) #this skips the first line (header)

for record in csvfile:

    
        #print(record) record is a list object
        print('student ID: ', record[0])
        print('fname: ', record[1])
        print('lname: ', record[2])
        print('city: ', record[3])
        print('country: ', record[4])
        print('phone: ', record[5])

        input()

