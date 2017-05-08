import pprint

a = u'bats\u00E0'

pprint.pformat(a) # Works
str(a)            # Works
print(a)          # UnicodeEncodeError: 'ascii' codec can't encode character '\xe0' in position 4: ordinal not in range(128)
