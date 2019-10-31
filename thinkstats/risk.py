import sys
import survey
import Pmf

# Create pregnancy 
# split it in alive, first, others
# create pmfs
# process pmfs

def PartitionTable(table):
  alive = survey.Pregnancies()
  first = survey.Pregnancies()
  other = survey.Pregnancies()

  for record in table.records:
    if record.outcome != 1:
      continue
    
    alive.AddRecord(record)

    if record.birthord == 1:
      first.AddRecord(record)
    else:
      other.AddRecord(record)
  
  return alive, first, other

def MakeTables(data_dir):
  table = survey.Pregnancies()
  table.ReadRecords()

  alive, first, other = PartitionTable(table)

  return alive, first, other

def MakePmf(*tables):
  for table in tables:
    table.pmf = Pmf.MakePmfFromList([x.prglength for x in table.records])

def Probability(pmf,bin_range):
  prob = 0.0
  for val, freq in pmf.Items():
    if val in bin_range:
      prob += freq
  
  return prob

def ProbEarly(pmf):
  return Probability(pmf,range(38))

def ProbOnTime(pmf):
  return Probability(pmf,range(38,41))

def ProbLate(pmf):
  return Probability(pmf,range(41,70))

def ProcessTables(*tables):
  for table in tables:
    table.probEarly = ProbEarly(table.pmf)
    table.probOnTime = ProbOnTime(table.pmf)
    table.probLate = ProbLate(table.pmf)

def RelativeRisk(data_dir='.'):

  alive, first, other = MakeTables(data_dir)
  MakePmf(alive,first,other)
  ProcessTables(alive, first, other)

  print 'Probabilities:'
  print 'Overall - Born Early:', alive.probEarly * 100
  print 'Overall - Born On Time:', alive.probOnTime * 100
  print 'Overall - Born Late:', alive.probLate * 100
  print 'First - Born Early:', first.probEarly * 100
  print 'First - Born On Time:', first.probOnTime * 100
  print 'First - Born Late:', first.probLate * 100
  print 'Other - Born Early:', other.probEarly * 100
  print 'Other - Born On Time:', other.probOnTime * 100
  print 'Other - Born Late:', other.probLate * 100

  print 'Relative Risks:'
  print 'Born Early:', first.probEarly / other.probEarly
  print 'Born On Time:', first.probOnTime / other.probOnTime
  print 'Born Late:', first.probLate / other.probLate

def main():
  RelativeRisk()

if __name__ == '__main__':
  main()
