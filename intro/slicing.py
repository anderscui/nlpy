saying = ['After', 'all', 'is', 'said', 'and', 'done',
          'more', 'is', 'said', 'than', 'done']

tokens = set(saying)
tokens = sorted(tokens)

## the last 2 items alphabetically
print(tokens[-2:])