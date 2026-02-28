#Why does this function always print 0, and how do you fix it?
def count_items(items):
    count = 0
    for item in items:
        count + 1
    return count

print(count_items([10, 20, 30]))

