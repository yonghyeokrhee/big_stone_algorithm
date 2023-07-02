_ , param = map(int, input().split())
nums = list(map(int, input().split()))

avg = []
for i in range(len(nums)-param):
    avg.append(sum(nums[i:i+param]))
print(max(avg))
