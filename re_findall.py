import re

text = 'The rain in Germany and Spain'

found = re.findall('ai', text)
print(f'{type(found)=}')
print(f'{found=}')
