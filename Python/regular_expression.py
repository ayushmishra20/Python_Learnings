# not use for basic matches

import re
pattern = "lore"
text = '''
lore ipsum loren ipsum dolor

'''

match = re.search(pattern, text) # stops for 1st occurance
print(match)

match2 = re.finditer(pattern, text)
for match in match2:
    print(text[match.span()[0]:match.span()[1]])