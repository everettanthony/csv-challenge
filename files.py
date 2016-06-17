import csv, os

# Function to grab the CSV files and prep them for the CSV Reader.
def filelist(*files):
    for f in files:
    	global fname
    	fname = os.path.basename(f) # Assign the file names to the fname variable.
        with open(f) as fobj:
        	next(fobj)
        	for line in fobj:
        		yield line

# Write the data from the collected CSV files into a new CSV file.
writer = csv.writer(open('docs/merged.csv', 'wb'))
writer.writerow(['email_hash', 'category', 'filename'])
for row in csv.reader(filelist('docs/clothing.csv', 'docs/accessories.csv', 'docs/household_cleaners.csv')):
	row.append(fname) # Append the new filename column.
	writer.writerow(row)