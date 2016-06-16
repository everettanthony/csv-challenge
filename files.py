import csv, os

def list(*files):
    for f in files:
    	global fname
    	fname = os.path.basename(f)
        with open(f) as fobj:
        	next(fobj)
        	for line in fobj:
        		yield line

writer = csv.writer(open('docs/merged.csv', 'wb'))
writer.writerow(['email_hash', 'category', 'filename'])
for row in csv.reader(list('docs/clothing.csv', 'docs/accessories.csv', 'docs/household_cleaners.csv')):
	row.append(fname)
	writer.writerow(row)