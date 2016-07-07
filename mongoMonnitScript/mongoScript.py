import csv
from datetime import datetime
from pymongo import MongoClient

client = MongoClient("127.0.0.1", port = 27017)

# change this to the db you want to use
db = client.script_test

# csv file to pull data from 
with open('monnitTest.csv', 'rb') as csvfile:

	reader = csv.reader(csvfile)
	try: 
		for row in reader:
			brand = row[0]
			model = row[1]
			serial_number = row[2]
			status = row[3]
			notes = row[4]

			# this should be the collection you want to insert into 
			db.test1Col.insert_one({
				"brand" : brand,
				"model" : model,
				"serial_number" : serial_number,
				"status" : status,
				"extra_info" : {
					"notes" : notes,
				},
				"added_to_lib" : datetime.now()
			});

	except csv.Error as err:
		client.close()
		sys.exit('file %s, line %d: %s' % (csvfile, reader.line_num, err))

	client.close()