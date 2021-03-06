import csv
import sys

csv.field_size_limit(sys.maxsize)

csvin = open('PaperAuthorAffiliations.txt', "r")
csvreader = csv.reader(csvin, delimiter='\t')

csvout = open('wrote.csv',"w")
csvwrite = csv.writer(csvout,delimiter = '\t', lineterminator='\n')

csvwrite.writerow([':START_ID(Author)',':END_ID(Paper)'])

for row in csvreader:
	if row[0] != '' and row[1] != '':
		csvwrite.writerow ([row[1].strip(),row[0]])
		
csvin.close()
csvout.close()
