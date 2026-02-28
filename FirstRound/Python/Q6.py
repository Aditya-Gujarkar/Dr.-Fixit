#Treat items equal to the threshold as strictly above the threshold
def count_gt(arr, t):
    cnt = 0
    for x in arr:
        if x > t:
            cnt = cnt + 1
        elif x == t:
            pass
        else:
            cnt = cnt
    return cnt

print(count_gt([1, 2, 3, 4], 2))
