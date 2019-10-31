import sys
import Pmf

def PmfMean(pmf):
  # Mean with a PMF can be calculated as follows:
  # mu = sum[pi * xi]
  # where pi is the probability of item i
  # and xi is the value of item i
  mu = 0.0
  for val, prob in pmf.Items():
    mu += val * prob
  
  return mu

def PmfVar(pmf):
  # Variance with a PMF can be calculated as follows:
  # var = sum[pi*(xi - mu)**2]
  # where pi is the probability of item i
  # and xi is the value of item i
  # and mu is the mean
  var = 0.0
  mu = PmfMean(pmf)
  for val, prob in pmf.Items():
    var += prob*(val - mu)**2
  
  return var

def main(*list):
  list = [int(x) for x in list]
  pmf = Pmf.MakePmfFromList(list)
  mu = PmfMean(pmf)

  print 'Mean from Pmf:', mu

  var = PmfVar(pmf)

  print 'Variance from Pmf:', var

if __name__ == '__main__':
  main(*sys.argv[1:])