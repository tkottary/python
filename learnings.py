# Linkedin Python course

# to print first friday of every month
print (" meeting date are as follows ")
for i in range(1,13):
    cal  = calendar.monthcalendar(2019,i)
    weekone = cal[0]
    weektwo = cal[1]
      
    if weekone[calendar.FRIDAY] != 0:
          meetday = weekone[calendar.FRIDAY]
    else:
          meetday = weektwo[calendar.FRIDAY]

    print("%10s %2d" %(calendar.month_name[i], meetday)) 


### How many days until April Fools' Day?

today= date.today()
afd = date(today.year,4,1)
if afd< today:
    print(" April fools day already went by %d days ago" %((today-afd).days))
    afd= afd.replace(year=today.year+1)
# Now calculate the amount of time until April Fool's Day  

imetoAfd= afd - today
print (" Its just ",timetoAfd.days, "days away")


#### version of python that is used

import platform
print('This is python version {}'.format(platform.python_version()))

## to get the maximum num in Python

float('inf')

### to get the minimum no in python
float('-inf')
