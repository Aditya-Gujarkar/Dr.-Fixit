#ZeroDivisionError
def count_above_average(nums):
    avg = sum(nums) / len(nums)
    cnt = 0
    for x in nums:
        if x > avg:
            cnt += 1
    return cnt
