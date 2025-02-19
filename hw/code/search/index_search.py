from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words
import re

def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    d = defaultdict(set)
    for i in range(0, len(files)):
        words = re.findall(r'\w+', get_text(files[i]))
        for word in words:
            d[word.lower()].add(i)
    return d

def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    first = True
    common_files_index = set()
    for term in terms:
        if first == True:
            first = False
            if term not in index.keys():
                continue
            common_files_index = index[term]
        else:
            if common_files_index:
                common_files_index = common_files_index.intersection(index[term])
    
    result = []
    if common_files_index:
        for i in common_files_index:
            result.append(files[i])

    return result

