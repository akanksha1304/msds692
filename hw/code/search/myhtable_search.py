# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from htable import *
from words import get_text, words
import re

def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    table = htable(4011)
    for i in range(0, len(files)):
        texts = re.findall(r'\w+', get_text(files[i]))
        for text in texts:
            htable_put(table, text.lower(), i)

    return table

def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    first = True
    common_files_index = set()
    for term in terms:
        word = term.lower()
        if first == True:
            first = False
            key_index = bucket_indexof(index, word)
            if key_index == -1:
                continue
            common_files_index = htable_get(index, word)
        else:
            if common_files_index:
                common_files_index = common_files_index.intersection(htable_get(index, word))
    
    result = []
    if common_files_index:
        for i in common_files_index:
            result.append(files[i])

    return result
