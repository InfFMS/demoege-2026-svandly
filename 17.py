nums = [int(x) for x in open('DEMO_17.txt')]

mini = min(x for x in nums if x > 9 and x < 100)

max_sum = 0

count = 0

for i in range(len(nums)):
    for j in range(len(nums)):
        if i != j:
            if (nums[i] + nums[j]) % mini == 0:
                if max(nums[j], nums[i]) > 99 and 9 < min(nums[j], nums[i]) < 100:
                    count +=1
                    if nums[i] + nums[j] > max_sum:
                        max_sum = nums[i] + nums[j]
                elif min(nums[j], nums[i]) < 10 and 9 < max(nums[j], nums[i]) < 100:
                    count += 1
                    if nums[i] + nums[j] > max_sum:
                        max_sum = nums[i] + nums[j]


print(count, max_sum)
