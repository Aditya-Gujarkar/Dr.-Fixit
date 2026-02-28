items = ['a', '', 'b', '', 'c']
for s in items:
    if s == '':
        items.remove(s)
print(items)
