import sys
import math

def Mean(t):
  return float(sum(t)) / len(t)

def Variance(t):
  mu = Mean(t)
  deviations = [(x - mu)**2 for x in t] 
  return float(sum(deviations)) / len(t)

def StandardDeviation(t):
  return math.sqrt(Variance(t))

def main(*pumpkins):
  t = [int(x) for x in pumpkins]
  mu = Mean(t)
  var = Variance(t)
  stdDev = StandardDeviation(t)

  print 'Mean:', mu
  print 'Variance:', var
  print 'Standard Deviation:', stdDev

if __name__ == '__main__':
  main(*sys.argv[1:])