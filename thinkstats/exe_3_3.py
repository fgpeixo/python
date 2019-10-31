import sys
import math

def Percentile(percentile_rank, scores):
  percentile_index = int(math.ceil((percentile_rank / 100.0) * len(scores))) - 1
  return scores[percentile_index]

def main():
  scores = [55, 66, 77, 88, 99]
  percentile_rank = 80
  print  Percentile(percentile_rank, scores)

if __name__ == '__main__':
  main()