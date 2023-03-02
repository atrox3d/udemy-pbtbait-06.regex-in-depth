import re

text = 'The rain in Germany'

# find the first space in the string, returns re.Match
match = re.search(r'\s', text)

if match:
    print("yes, we have a match")
    print(f'{type(match)=}')
    print(f'{match=}')
    print(f'{match.start()=}')
    print(f'{match.end()=}')
    print(f'{match.pos=}')
    print(f'{match.endpos=}')
    print(f'{match.re=}')
    print(f'{match.string=}')
else:
    print('no match')
