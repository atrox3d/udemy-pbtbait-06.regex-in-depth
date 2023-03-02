import re

text = "The match in Germany"
found = re.search('^the.*germany', text, re.IGNORECASE)

if found:
    print("yes, we have a match")
    print(f'{type(found)=}')
    print(f'{found=}')
    print(f'{found.group()=}')
    print(f'{found.start()=}')
    print(f'{found.end()=}')
    print(f'{found.groupdict()=}')
    print(f'{found.pos=}')
    print(f'{found.endpos=}')
    print(f'{found.re=}')
    print(f'{found.lastgroup=}')
    print(f'{found.lastindex=}')
    print(f'{found.lastindex=}')
    print(f'{found.string=}')
else:
    print('no match')
