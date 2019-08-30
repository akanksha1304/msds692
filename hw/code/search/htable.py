"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    table = []
    for i in range(0, nbuckets):
        table.append([])
    return table


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    if ((type(o) is int) or (type(o) is str)) == False:
        return None
    elif (type(o) is int):
        return o
    else:
        h = 0
        for i in range(0, len(o)):
            h = h + h*31 + ord(o[i])
        return h


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    bucket = table[hashcode(key) % len(table)]
    for i in range(0, len(bucket)):
        if bucket[i][0] == key:
            return i
    return -1



def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    bucket = table[hashcode(key) % len(table)]
    for i in range(0, len(bucket)):
        if bucket[i][0] == key:
            if value not in bucket[i][1]:
                bucket[i][1].add(value)
            return
    
    s = {value}
    t = (key, s)
    bucket.append(t)
        

def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    bucket = table[hashcode(key) % len(table)]
    for i in range(0, len(bucket)):
        if bucket[i][0] == key:
            return bucket[i][1]
    return None

def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    hstr = ''
    for i in range(0,len(table)):
        bucket = table[i]
        if i < 10:
            hstr = hstr + '000' + str(i) + '->'
        elif i < 100:
            hstr = hstr + '00' + str(i) + '->'
        elif i < 1000:
            hstr = hstr + '0' + str(i) + '->'
        else:
            hstr = hstr + str(i) + '->'

        for j in range(0, len(bucket)):
            hstr = hstr + bucket[j][0] + ':' + str(bucket[j][1]) + ','
        if len(bucket) > 0:
            hstr = hstr[0:len(hstr)-1] + '\n'
        else:
            hstr = hstr + '\n'

    print(hstr)

def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    hstr = '{'
    for i in range(0,len(table)):
        bucket = table[i]
        for j in range(0, len(bucket)):
            hstr = hstr + bucket[j][0] + ':' + str(bucket[j][1]) + ', '
        
    if len(hstr) > 2:
        hstr = hstr[0:len(hstr)-2] + '}'
    else:
        hstr = hstr + '}'
    print(hstr)