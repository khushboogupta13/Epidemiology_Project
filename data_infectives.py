import sys
from builtins import any

raw_data = [line.strip() for line in open("covid_data_uk.txt")]
data = raw_data[1:]
birmingham = []
staffordshire = []
coventry = []
wolverhampton = []
dudley = []
solihull= []
sandwell = []
walsall = []
warwickshire = []
worcestershire = []

def make_date():
    dates = []
    for date in range(1, 10):
        dates.append("0" + str(date))
    for date in range(10, 32):
        dates.append(str(date))
    march = ["2020-03-" + y for y in dates[1:]]
    april = ["2020-04-" + y for y in dates[:-1]]
    may = ["2020-05-" + y for y in dates]
    june = ["2020-06-" + y for y in dates[:20]]
    return march + april + may + june

def rem_unn(string):
    return string.replace("England,", "").replace("E10000034,", "").replace("E10000031,", "").replace("E08000030,", "").replace("E08000028,", "").replace("E08000029,", "").replace("E08000027,", "").replace("E08000031,", "").replace("E08000026,", "").replace("E10000028,", "").replace("E08000025,", "")

for i in data:
    i = rem_unn(i)
    if "Birmingham" in i:
        birmingham.append(i)
    elif "Staffordshire" in i:
        staffordshire.append(i)
    elif "Coventry" in i:
        coventry.append(i)
    elif "Wolverhampton" in i:
        wolverhampton.append(i)
    elif "Dudley" in i:
        dudley.append(i)
    elif "Solihull" in i:
        solihull.append(i)
    elif "Sandwel" in i:
        sandwell.append(i)
    elif "Walsall" in i:
        walsall.append(i)
    elif "Warwickshire" in i:
        warwickshire.append(i)
    elif "Worcestershire" in i:
        worcestershire.append(i)

birmingham_inf = [int(_.split(",")[2]) for _ in birmingham]
staffordshire_inf = [int(_.split(",")[2]) for _ in staffordshire]
coventry_inf = [int(_.split(",")[2]) for _ in coventry]
wolverhampton_inf = [int(_.split(",")[2]) for _ in wolverhampton]
dudley_inf = [int(_.split(",")[2]) for _ in dudley]
solihull_inf = [int(_.split(",")[2]) for _ in solihull]
sandwell_inf = [int(_.split(",")[2]) for _ in sandwell]
walsall_inf = [int(_.split(",")[2]) for _ in walsall]
warwickshire_inf = [int(_.split(",")[2]) for _ in warwickshire]
worcestershire_inf = [int(_.split(",")[2]) for _ in worcestershire]

dates = make_date()

inf_per_date = {date: 0 for date in dates}

initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in birmingham):
        birmingham_inf.insert(date, initial)
    else:
        initial = birmingham_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in staffordshire):
        staffordshire_inf.insert(date, initial)
    else:
        initial = staffordshire_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in coventry):
        coventry_inf.insert(date, initial)
    else:
        initial = coventry_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in wolverhampton):
        wolverhampton_inf.insert(date, initial)
    else:
        initial = wolverhampton_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in dudley):
        dudley_inf.insert(date, initial)
    else:
        initial = dudley_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in solihull):
        solihull_inf.insert(date, initial)
    else:
        initial = solihull_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in sandwell):
        sandwell_inf.insert(date, initial)
    else:
        initial = sandwell_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in walsall):
        walsall_inf.insert(date, initial)
    else:
        initial = walsall_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in warwickshire):
        warwickshire_inf.insert(date, initial)
    else:
        initial = warwickshire_inf[date]
initial = 0
for date in range(len(dates)):
    if not any(dates[date] in x for x in worcestershire):
        worcestershire_inf.insert(date, initial)
    else:
        initial = worcestershire_inf[date]

for date in range(len(dates)):
    inf_per_date[dates[date]] += birmingham_inf[date]
    inf_per_date[dates[date]] += staffordshire_inf[date]
    inf_per_date[dates[date]] += coventry_inf[date]
    inf_per_date[dates[date]] += wolverhampton_inf[date]
    inf_per_date[dates[date]] += dudley_inf[date]
    inf_per_date[dates[date]] += solihull_inf[date]
    inf_per_date[dates[date]] += sandwell_inf[date]
    inf_per_date[dates[date]] += walsall_inf[date]
    inf_per_date[dates[date]] += warwickshire_inf[date]
    inf_per_date[dates[date]] += worcestershire_inf[date]

print(inf_per_date)
