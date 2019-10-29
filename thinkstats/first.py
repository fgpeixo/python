import survey

table = survey.Pregnancies()
table.ReadRecords()

print 'Number of pregnancies', len(table.records)

live_births_first = 0
live_births_others = 0

count_first = 0
count_others = 0
sum_prglen_first = 0
sum_prglen_others = 0

for record in table.records:
  if record.outcome == 1:
    if record.birthord == 1:
      live_births_first += 1
      sum_prglen_first += record.prglength
    else:
      live_births_others += 1
      sum_prglen_others += record.prglength

avg_prglen_first = sum_prglen_first / live_births_first
avg_prglen_others = sum_prglen_others / live_births_others
diff_avg_prglen = avg_prglen_first - avg_prglen_others

print 'Live births for first babies:', live_births_first
print 'Live births for other babies:', live_births_others

print 'Average pregnancy length for first babies:', avg_prglen_first
print 'Average pregnancy length for other babies:', avg_prglen_others
print 'Difference in pregnancy length (first - others):', diff_avg_prglen