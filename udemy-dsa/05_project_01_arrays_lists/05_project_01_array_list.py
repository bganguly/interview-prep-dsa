numdays = int(input('how many days: '))
temp = []
for i in range(numdays):
    nextDay = int(input('Day ' + str(i+1) + ' high temp: '))
    temp.append(nextDay)
avgTemp = sum(temp)/numdays
print (' avg temperarture is : ', avgTemp)
high_temp = [ i for i in temp if i > avgTemp ]    
print(' number of days higher than avg temperarture is : ', len(high_temp))
