import sys
import mycsv
import json

def json2csv(jdata):
	header = jdata["headers"]
	header_str = header[0]
	for i in range(1,len(header)):
		header_str = header_str + ',' + header[i]
	print(header_str)

	for i in range(0, len(jdata["data"])):
		row = jdata["data"][i]
		row_str = row[header[0]]
		for j in range(1, len(header)):
			row_str = row_str + ',' + row[header[j]]
		print(row_str)

json2csv(json.loads(mycsv.getdata()))