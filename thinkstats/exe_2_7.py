import sys
import Pmf
import survey
import matplotlib.pyplot as pyplot

# Plot chart for the probability of a baby to be born on week x 
# given it was not born prior to week x

def PartitionTable(table):
  first = survey.Pregnancies()
  other = survey.Pregnancies()

  for record in table.records:
    if record.outcome != 1:
      continue
    
    if record.birthord == 1:
      first.AddRecord(record)
    else:
      other.AddRecord(record)
  
  return first, other

def MakeTables(data_dir='.'):
  table = survey.Pregnancies()
  table.ReadRecords()

  first, other = PartitionTable(table)

  return table, first, other

def GeneratePmf(*tables):
  for table in tables:
    table.pmf = Pmf.MakePmfFromList([r.prglength for r in table.records])

def ProbBornInWeek(pmf, week):
  week_pmf = {}
  for i in range(week,51):
    week_pmf[i] = pmf.d.get(i,0)

  total = sum(week_pmf.values())
  if total == 0.0:
    return 0
  else:
    return 100 * week_pmf.get(week) / total #Normalized probability for week

def GenerateProbBornPerWeek(*tables):
  for t in tables:
    t.probBorbPerWeek = []
    for week in range(51):
      t.probBorbPerWeek.append(ProbBornInWeek(t.pmf,week))

def PlotProbabilities():
  print 'Plotting...'
  table, first, other = MakeTables()
  GeneratePmf(first,other)
  GenerateProbBornPerWeek(first,other)
  
  width = 0.4
  x_first = [x - width/2 for x in range(51)]
  x_other = [x + width/2 for x in range(51)]
  pyplot.bar(x_first,first.probBorbPerWeek,width,label='First')
  pyplot.bar(x_other,other.probBorbPerWeek,width,label='Other')
  pyplot.xticks(range(51))
  pyplot.legend()
  pyplot.show()


def main():
  PlotProbabilities()

if __name__ == '__main__':
  main()