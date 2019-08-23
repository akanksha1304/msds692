import sys
import mycsv
import untangle

def xml2csv(data):
	header = data.file.headers.cdata.split(',')
	header_str = header[0]
	for i in range(1,len(header)):
		header_str = header_str + ',' + header[i]
	print(header_str)

	for i in range(0, len(data.file.data.record)):
		row = data.file.data.record[i]
		row_str = row.children[0].cdata
		for j in range(1, len(row.children)):
			row_str = row_str + ',' + row.children[j].cdata
		print(row_str)


xml2csv(untangle.parse(mycsv.getdata()))