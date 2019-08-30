# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

import re
from words import get_text, words

"""
Given a list of fully-qualified filenames, return a list of them
whose file contents has all words in terms as normalized by your words() function.
Parameter terms is a list of strings.
Perform a linear search, looking at each file one after the other.
"""
def linear_search(files, terms):
	result = []
	for i in range(0, len(files)):
		text = re.findall(r"\w+", get_text(files[i]))
		all_present = True
		for j in range(0, len(terms)):
			term = terms[j]
			present = False
			for k in text:				
				if k.lower() == term:
					present = True
					break

			if present == False:
				all_present = False
				break
		if  all_present == True:
			result.append(files[i])

	return result



