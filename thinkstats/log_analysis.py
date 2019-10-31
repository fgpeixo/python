import sys
import re
import datetime as dt
import matplotlib.pyplot as pyplot

def MakeLogFromFile(filename):
  file = open(filename, 'rU')
  log = []
  timestamp = 0
  error_code = 0
  fault_string = ''
  for row in file:
    #search for timestamp or message and faultstring
    m = re.search(r'\"timestamp\":\s(\d+),',row)
    if m:
      timestamp = int(m.group(1)[:-3])

    m = re.search(r'message\\\":\\\"(\d\d\d)\s-\s\S*faultstring\\\\\\\":\\\\\\\"([\w\s]+)',row)
    if m:
      error_code = int(m.group(1))
      fault_string = m.group(2)

    if timestamp and error_code and fault_string:
      log.append((timestamp,error_code,fault_string))  
      timestamp = 0
      error_code = 0
      fault_string = ''
  
  return log

def PrepareChart(log,option=''):
  xs = []
  ys = []
  date_time = ''
  dict = {}

  for ts, ec, fault_string in log:
    if option == 'd':
      date_time = dt.datetime.fromtimestamp(ts).date()
    elif option == 'h':
      dtobj = dt.datetime.fromtimestamp(ts)
      hour = str(dtobj.hour)
      if len(hour) == 1:
        hour = '0' + hour
      date_time = str(dtobj.day) + '/' + str(dtobj.month) + '/' + str(dtobj.year) + ' ' + hour
    elif option == 'm':
      dtobj = dt.datetime.fromtimestamp(ts)
      hour = str(dtobj.hour)
      minute = str(dtobj.minute)
      if len(hour) == 1:
        hour = '0' + hour
      if len(minute) == 1:
        minute = '0' + minute
      date_time = str(dtobj.day) + '/' + str(dtobj.month) + '/' + str(dtobj.year) + ' ' + hour + ':' + minute
    else:
      date_time = dt.datetime.fromtimestamp(ts).ctime()

    dict[date_time] = dict.get(date_time,0) + 1

  xs_tuple, ys_tuple = zip(*sorted(dict.items()))
  xs = [x for x in xs_tuple]
  ys = [y for y in ys_tuple]

  return xs, ys

def main():

  args = sys.argv[1:]
  if not args:
    print 'usage: [--minute | --hour | --day] filename'
    sys.exit(1) 

  option = ''
  if args[0] == '--day':
    option = 'd'
    del args[0]
  elif args[0] == '--minute':
    option = 'm'
    del args[0]
  elif args[0] == '--hour':
    option = 'h'
    del args[0]

  filename = args[0] 

  log = MakeLogFromFile(filename)
  xs, ys = PrepareChart(log,option)

  pyplot.bar(xs, ys)
  pyplot.show()

if __name__ == '__main__':
  main()