import csv

infile = open('steps.csv', 'r')
csvfile = csv.reader(infile)
next(csvfile)

outfile = open('avg_steps.csv', 'w')

for record in csvfile:
    i = 0
    if record[0] == 1:
        addition = sum(record[1])
        i += 1
        outfile.write('January, ' + addition/i)
    elif record[0]==2:
        i += 1
        outfile.write('February, ' + sum(record[1])/i)
    elif record[0] == 3:
        i += 1
        outfile.write('March, ' + sum(record[1])/i)
    elif record[0] == 4:
        i += 1
        outfile.write('April, ' + sum(record[1])/i)
    elif record[0] == 5:
        i += 1
        outfile.write('May, ' + sum(record[1])/i)
    elif record[0] == 6:
        i += 1
        outfile.write('June, ' + sum(record[1])/i)
    elif record[0] == 7:
        i += 1
        outfile.write('July, ' + sum(record[1])/i)
    elif record[0] == 8:
        i += 1
        outfile.write('August, ' + sum(record[1])/i)
    elif record[0] == 9:
        i += 1
        outfile.write('September, ' + sum(record[1])/i)
    elif record[0] == 10:
        i += 1
        outfile.write('October, ' + sum(record[1])/i)
    elif record[0] == 11:
        i += 1
        outfile.write('November, ' + sum(record[1])/i)
    elif record[0] == 12:
        i += 1
        outfile.write('December, ' + sum(record[1])/i)

outfile.close