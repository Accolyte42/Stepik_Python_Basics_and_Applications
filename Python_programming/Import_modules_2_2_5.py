from datetime import datetime, date, time, timedelta

dt = input().split()
tdel = int(input())
# print(type(dt), dt)
for i in range(len(dt)):
    dt[i] = int(dt[i])
# print(dt)
ddt = date(dt[0], dt[1], dt[2])
# print(ddt)

tdel = timedelta(days=tdel)

req_time = ddt+tdel
print(req_time.year, req_time.month, req_time.day)

# dt1 = datetime.date.strfdate(dt, '%y %m %d')
# print(dt1)


# import datetime
# inp = datetime.datetime.strptime(input(), "%Y %m %d")
# inp += datetime.timedelta(days=int(input()))
# print(f'{inp.year} {inp.month} {inp.day}')






