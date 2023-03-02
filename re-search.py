import re

text = "The match in Germany"
match = re.search('^the.*germany', text, re.IGNORECASE)

if match:
    print("yes, we have a match")
    print(f'{type(match)=}')
    print(f'{match=}')
    print(f'{match.group()=}')
    print(f'{match.start()=}')
    print(f'{match.end()=}')
    print(f'{match.groupdict()=}')
    print(f'{match.pos=}')
    print(f'{match.endpos=}')
    print(f'{match.re=}')
    print(f'{match.lastgroup=}')
    print(f'{match.lastindex=}')
    print(f'{match.lastindex=}')
    print(f'{match.string=}')
else:
    print('no match')
