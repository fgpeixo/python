import sys
import Pmf
import matplotlib.pyplot as pyplot

def GetFreq((val, freq)):
  return freq

def Mode(hist):
  sorted_hist = sorted(hist.Items(),key=GetFreq)
  val , freq = sorted_hist[-1]
  return val

def AllMode(hist):
  return reversed(sorted(hist.Items(),key=GetFreq))

def main(*list):
  # Create Hist from list
  hist = Pmf.MakeHistFromList(list)
  
  mo = Mode(hist)
  print 'Mode:', mo

  allMode = AllMode(hist)
  print 'All Modes:'
  for val, freq in allMode:
    print 'Value:', val, '=> Frequence:', freq

  vals, freqs = hist.Render()
  rectangles = pyplot.bar(vals, freqs)
  pyplot.show()

if __name__ == '__main__':
  main(*sys.argv[1:])