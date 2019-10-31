import uuid

file = open('areas.txt','rU')
for row in file:
  if row[-1] == '\n':
    print row[:-1] + ',' + str(uuid.uuid4())
  else:
    print row + ',' + str(uuid.uuid4())