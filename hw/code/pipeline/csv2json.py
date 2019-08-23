import sys
import mycsv

def csv2json(data):
	print('{')

	sentences = data.split('\n')
	header = sentences[0].split(',')

	header_str = '\t\"headers\":[\"' + header[0] + '\"'
	for i in range(1, len(header)):
		header_str = header_str + ', \"' + header[i] + '\"'

	header_str = header_str + '],'
	print(header_str)

	print('\t\"data\":[')
	for i in range(1, len(sentences)):
		row = sentences[i].split(',')
		
		print('\t\t{')
		row_str = '\t\t\t'
		for j in range(0, len(row)):
			if j != (len(row)-1) :
				row_str = row_str + '\"' + header[j] + '\":\"' + row[j] + '\", '
			else:
				row_str = row_str + '\"' + header[j] + '\":\"' + row[j] + '\"'

		print(row_str)

		if i != len(sentences)-1 :
			print('\t\t},')
		else:
			print('\t\t}')
	print('\t]')
	print('}')

csv2json(mycsv.getdata())