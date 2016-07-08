import csv
from datetime import datetime
from pymongo import MongoClient

client = MongoClient("127.0.0.1", port = 27017)

# change this to the db you want to use
db = client.script_test

# csv file to pull data from 
with open('Monnit_Order_to_Add_to_Ebla_Batch_1.csv', 'rb') as csvfile:

	reader = csv.reader(csvfile)
	next(reader)	#skip line that has headers
	try: 
		for row in reader:
			brand = row[0]
			model = row[1]
			serial_number = row[2]
			status = 'IN'
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
		csvfile.close()
		sys.exit('file %s, line %d: %s' % (csvfile, reader.line_num, err))

	client.close()
	csvfile.close()

# Data used to test this
# Monnit,MNG-9-EG (Ethernet),104556,IN,EthernetGateway; Sensor Code - IMLHNT
# Monnit,MNG-10-EG (Ethernet),104557,IN,EthernetGateway; Sensor Code - ASDFGD
# Monnit,MNG-11-EG (Ethernet),104558,IN,EthernetGateway; Sensor Code - QWERGA
# Monnit,MNG-12-EG (Ethernet),104559,IN,EthernetGateway; Sensor Code - IOJHNM
# Monnit,MNG-13-EG (Ethernet),104560,IN,EthernetGateway; Sensor Code - QWEPRI