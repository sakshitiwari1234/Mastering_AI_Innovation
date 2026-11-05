# what is json

# javascript object notation.

# json is a data exchange format similar to XML.''

# {
#     "name": "tom", "address":"1 green street ,NY"




# }

# XML
# <name>tom</name>
# <address> green street, NY</address>
# <phone> 2342324342</phone>

# 1. to create address book and write some r

book = {}
book['tom'] = {
    'name': 'tom', 'address':'1 red street', 'phone':5235235
}

book['bob'] = {
    'name':'bob',
    'address': ' new york',
    'phone': 34224
}

import json
s = json.dumps(book)
print(s)

# // we are writing this dictionary to a file.
with open ("c://data//book.txt", "w") as f:
    f.write(s)












