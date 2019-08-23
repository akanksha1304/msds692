#!/bin/bash

INPUT=$1
OUTPUT=$2
MYSRC=.  # current directory

for f in $INPUT/*.csv
do
	NAME=$(basename -s '.csv' $f)
	echo "Test" $NAME
	python3 csv2html.py $f > /tmp/csv2html-$NAME.html
	echo -n "   csv2html: "
	python3 $MYSRC/htmlcompare.py $OUTPUT/$NAME.html /tmp/csv2html-$NAME.html

	python3 csv2xml.py $f > /tmp/csv2xml-$NAME.xml
	echo -n "   csv2xml: "
	python3 $MYSRC/xmlcompare.py $OUTPUT/$NAME.xml /tmp/csv2xml-$NAME.xml

	python3 csv2json.py $f > /tmp/csv2json-$NAME.json
	echo -n "   csv2json: "
	python3 $MYSRC/jsoncompare.py $OUTPUT/$NAME.json /tmp/csv2json-$NAME.json

	# test xml from correct output dir -> CSV
	python3 xml2csv.py $OUTPUT/$NAME.xml > /tmp/xml2csv-$NAME.csv
	echo -n "   xml2csv: "
	python3 $MYSRC/csvcompare.py $INPUT/$NAME.csv /tmp/xml2csv-$NAME.csv

	python3 json2csv.py $OUTPUT/$NAME.json > /tmp/json2csv-$NAME.csv
	echo -n "   json2csv: "
	python3 $MYSRC/csvcompare.py $INPUT/$NAME.csv /tmp/json2csv-$NAME.csv

	python3 xml2csv.py $OUTPUT/$NAME.xml | python3 csv2xml.py > /tmp/xml2csv-csv2xml-$NAME.xml
	echo -n "   xml2csv|csv2xml: "
	python3 $MYSRC/xmlcompare.py $OUTPUT/$NAME.xml /tmp/xml2csv-csv2xml-$NAME.xml

	python3 json2csv.py $OUTPUT/$NAME.json | python3 csv2json.py > /tmp/json2csv-csv2json-$NAME.json
	echo -n "   json2csv|csv2json: "
	python3 $MYSRC/jsoncompare.py $OUTPUT/$NAME.json /tmp/json2csv-csv2json-$NAME.json
done
