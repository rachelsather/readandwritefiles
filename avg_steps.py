import csv

infile = open('steps.csv', 'r')
csvfile = csv.reader(infile)
next(csvfile)

outfile = open('avg_steps.csv', 'w')

for record in csvfile:
    jan = 0
    jan_counter = 0
    feb = 0
    feb_counter = 0
    mar = 0
    mar_counter = 0
    apr = 0
    apr_counter = 0
    may = 0
    may_counter = 0
    jun = 0
    jun_counter = 0
    jul = 0
    jul_counter = 0
    aug = 0
    aug_counter = 0
    sep = 0
    sep_counter = 0
    octo = 0
    octo_counter = 0
    nov = 0 
    nov_counter = 0
    dec = 0
    dec_counter = 0

    if record[0] == 1:
        jan += record[1]
        jan_counter += 1
    elif record[0] == 2:
        feb += record[1]
        feb_counter += 1
    elif record[0] == 3:
        mar += record[1]
        mar_counter += 1
    elif record[0] == 4:
        apr += record[1]
        apr_counter += 1
    elif record[0] == 5:
        may += record[1]
        may_counter += 1
    elif record[0] == 6:
        jun += record[1]
        jun_counter += 1
    elif record[0] == 7:
        jul += record[1]
        jul_counter += 1
    elif record[0] == 8:
        aug += record[1]
        aug_counter += 1
    elif record[0] == 9:
       sep += record[1]
       sep_counter += 1
    elif record[0] == 10:
        octo += record[1]
        octo_counter += 1
    elif record[0] == 11:
        nov += record[1]
        nov_counter += 1
    elif record[0] == 12:
        dec += record[1]
        dec_counter += 1

outfile.write('January, ' + jan/jan_counter)
outfile.write('February, ' + feb/feb_counter)
outfile.write('March, ' + mar/mar_counter)
outfile.write('April, ' + apr/apr_counter)
outfile.write('May, ' + may/may_counter)
outfile.write('June, ' +jun/jun_counter)
outfile.write('July, ' + jul/jul_counter)
outfile.write('August, ' + aug/aug_counter)
outfile.write('September, ' + sep/sep_counter)
outfile.write('October, ' + octo/octo_counter)
outfile.write('November, ' + nov/nov_counter)
outfile.write('December, ' + dec/dec_counter)

outfile.close