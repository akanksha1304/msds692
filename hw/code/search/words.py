import os
import re
import string
import numpy as np
import re

def filelist(root):
    """Return a fully-qualified list of filenames under root directory"""
    file_list = []
    for path, subdirs, files in os.walk(root):
        for name in files:
            if name.endswith('.txt'):
                filepath = os.path.join(path, name)
                file_list.append(filepath)

    return file_list


def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    
    html_content = "<!DOCTYPE html>\n<html>\n\t<body>"
    h2 = '\n\t<h2>Search results for <b>'
    for term in terms:
        h2 = h2 + term + ' '
    h2 = h2 + '</b> in ' + str(len(docs)) + ' files</h2>'

    html_content = html_content + h2

    n = np.minimum(100, len(docs))
    for i in range(0, n):
        doc = docs[i]
        doc_text_lines = get_text(doc).split('\n')
        doc_line_index = -1
        p = ''
        count = 0
        for term in terms:
            word = term.lower()
            for j in range(0,len(doc_text_lines)):  
                line = doc_text_lines[j].lower()   
                x = re.findall(r'\w+', line) 

                if (word in x) and (doc_line_index != j):
                    doc_line_index = j
                    p = p + line + '<br>' 
                    count = count + 1
                    break
            if count == 2:
                break

        k = re.findall(r'\w+', p)
        for w in k:
            for t in terms:
                if (t.lower() == w.lower()):
                    lst = []
                    p_copy = p
                    x = re.search(t.lower(), p_copy.lower())
                    sufx = 0
                    while (x is not None):
                        (start, end) = re.search(t.lower(), p_copy.lower()).span()
                        lst.insert(0, sufx+start)
                        lst.insert(0, sufx+end)
                        p_copy = p_copy[end:len(p_copy)]
                        x = re.search(t.lower(), p_copy.lower())
                        sufx = sufx + end
                    
                    for i in range(0, len(lst)-1, 2):
                        p = p[0:lst[i+1]] + '<b>' + p[lst[i+1]:lst[i]] + '</b>' + p[lst[i]:len(p)]
                    break

        pr = '\n\t\t<p><a href="file:///' + doc + '">' + doc + '</a><br>' + p + '<br>'
        html_content = html_content + pr
        
    html_content = html_content + '\n\t</body>'
    html_content = html_content + '\n</html>'
    return html_content


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]
