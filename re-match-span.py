import re

text = 'Python is a cross-platform programming language'
pattern = r'\b' \
          r'P' \
          r'\w' \
          r'+'
print(f'{pattern=}')
match = re.search(pattern, text)

if match:
    print("yes, we have a match\n")
    print(f'{match.string=}')
    print(f'{match.re=}')
    print(f'{type(match)=}')
    print(f'{match=}')
    print(f'{match.span()=}')
    print(f'{match.start()=}')
    print(f'{match.end()=}')
    print(f'{match.pos=}')
    print(f'{match.endpos=}')
else:
    print('no match')

