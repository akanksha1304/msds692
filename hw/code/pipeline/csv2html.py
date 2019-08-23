import sys
import mycsv

def csv2html(data):
	print('<html>')
	print('<body>')
	print('<table>')
	sentences = data.split('\n')
	header = sentences[0].split(',')

	header_str = '<tr><th>' + header[0]
	for i in range(1, len(header)):
		header_str = header_str + '</th><th>' + header[i]

	header_str = header_str + '</th></tr>'
	print(header_str)

	for i in range(1, len(sentences)):
		row = sentences[i].split(',')
		row_str = '<tr><td>' + row[0]
		for j in range(1, len(row)):
			row_str = row_str + '</td><td>' + row[j]
		row_str = row_str + '</td></tr>'
		print(row_str)

	print('</table>')
	print('</body>')
	print('</html>')

csv2html(mycsv.getdata())
