try:
    n = int(input())
except ValueError as e:
    print('0')

print(n * 2)
