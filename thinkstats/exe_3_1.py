import sys
import Pmf

def BiasedPmf(pmf,inverted=False):
  new_pmf = pmf.Copy()
  #Oversize the same by the class size
  #Or undersize by the class size
  for size, freq in new_pmf.Items():
    if inverted == False:
      new_pmf.Mult(size,size)
    else:
      new_pmf.Mult(size, 1.0/size)

  new_pmf.Normalize()
  return new_pmf

def ClassSizes():
  dict = {
    7 : 8,
    12 : 8,
    17 : 14,
    22 : 4,
    27 : 6,
    32 : 12,
    37 : 8,
    42 : 3,
    47 : 2,
  }

  deanPmf = Pmf.MakePmfFromDict(dict)
  print 'Dean Mean:', deanPmf.Mean()
  print 'Dean Variance:', deanPmf.Var()

  biasedPmf = BiasedPmf(deanPmf)
  print 'Biased Mean:', biasedPmf.Mean()
  print 'Biased Variance:', biasedPmf.Var()

  unBiasedPmf = BiasedPmf(biasedPmf,True)
  print 'Unbiased Mean:', unBiasedPmf.Mean()
  print 'Unbiased Variance:', unBiasedPmf.Var()

def main():
  ClassSizes()

if __name__ == '__main__':
  main()