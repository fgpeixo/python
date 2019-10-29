import sys
import math
import survey

def PartitionRecords(table):
  firsts = survey.Pregnancies()
  others = survey.Pregnancies()

  for record in table.records:
    if record.outcome != 1:
      continue

    if record.birthord == 1:
      firsts.AddRecord(record)
    else:
      others.AddRecord(record)

  return firsts, others

def MakeTables(data_dir):
  
  table = survey.Pregnancies()
  table.ReadRecords(data_dir)

  firsts, others = PartitionRecords(table)

  return table, firsts, others

def Mean(records):
  return float(sum(records)) / len(records)

def Variance(records):
  mu = Mean(records)
  deviations = [(x - mu)**2 for x in records]
  return float(sum(deviations)) / len(records)

def StandardDeviation(records):
  return math.sqrt(Variance(records))

def Process(table):
  table.prglengths = [rec.prglength for rec in table.records]
  table.n = len(table.records)
  table.mean = Mean(table.prglengths)
  table.variance = Variance(table.prglengths)
  table.stddev = StandardDeviation(table.prglengths)

def ProcessTables(*tables):
  for table in tables:
    Process(table)

def Summarize(data_dir):
  
  table, firsts, others = MakeTables(data_dir)
  ProcessTables(firsts,others)

  print 'Number of first babies:', firsts.n
  print 'Number of others:', others.n 

  print 'Mean gestation in weeks:'
  print 'First babies', firsts.mean
  print 'Other babies', others.mean
  print 'Difference in days:', (firsts.mean - others.mean) * 7.0
  print 'Difference in hours:', (firsts.mean - others.mean) * 7.0 * 24.0

  print 'Variance in weeks**2:'
  print 'First babies:', firsts.variance
  print 'Other babies:', others.variance

  print 'Standard deviation in weeks:'
  print 'First babies:', firsts.stddev
  print 'Other babies', others.stddev

def main(data_dir='.'):
  Summarize(data_dir)

if __name__ == '__main__':
  main(*sys.argv[1:])