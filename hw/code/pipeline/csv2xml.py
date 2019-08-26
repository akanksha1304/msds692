import sys
import mycsv

def csv2xml(data):
	print('<?xml version="1.0"?>')
	print('<file>')

	sentences = data.split('\n')
	header = sentences[0].split(',')

	header_str = '\t<headers>' + header[0]
	for i in range(1, len(header)):
		header_str = header_str + ',' + header[i]

	header_str = header_str + '</headers>'
	print(header_str)

	print('\t<data>')

	for i in range(1, len(sentences)):
		row = sentences[i].split(',')
		print('\t\t<record>')
		row_str = '<' + header[0].replace(' ','_') + '>' + row[0] + '</' + header[0].replace(' ','_') + '>'
		for j in range(1, len(row)):
			row_str = row_str + '<' + header[j].replace(' ','_') + '>' + row[j] + '</' + header[j].replace(' ','_') + '>'
		print('\t\t\t', row_str)
		print('\t\t</record>')
	print('\t</data>')
	print('</file>')

csv2xml(mycsv.getdata())