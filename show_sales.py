import sys


nums = sys.argv[1:]
with open('bakery.csv', encoding='utf-8') as fin:
    if len(nums) == 2:
        start_ind = int(nums[0])
        end_ind = int(nums[1])
    elif len(nums) == 0:
        start_ind = 0
        end_ind = sum(1 for line in fin)
        fin.seek(0)
    else:
        start_ind = int(nums[0])
        end_ind = sum(1 for line in fin)
    for ind, line in enumerate(fin, 1):
        if start_ind <= ind <= end_ind:
            print(line.strip())



