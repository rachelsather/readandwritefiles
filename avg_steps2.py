import csv

infile = open('steps.csv', 'r')
csvfile = csv.reader(infile)
next(csvfile)

outfile = open('avg_steps.csv', 'w')

days = [31,28,31,30,31,30,31,31,30,31,30,31]
month_name = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
monthCount = 0

for num in range(1, 13):
   
    totalSteps = 0
    count = 0
    average = 0
    
    for count in range(1, days[monthCount] + 1):
        steps = int(infile.readline())
        totalSteps += steps
  
    average = totalSteps / days[monthCount]
    
    outfile.write(months[monthCount] + ', ' + format(average, ',.1f'))
    
    monthCount = monthCount + 1

outfile.close