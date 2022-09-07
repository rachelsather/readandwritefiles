import csv

infile = open('customers.csv', 'r')
csvfile = csv.reader(infile)
next(csvfile)

outfile = open('customer_country.csv', 'w')

counter = 0

for record in csvfile:
    outfile.write(record[1] + ' ' + record[2] + ', ' + record[4] + '\n')
    counter += 1

outfile.write('\n' + 'Total number of customers: ' + str(counter))

outfile.close
