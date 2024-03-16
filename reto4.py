nums = [ 5, 3, 6, 8, -1]

nums.sort();

print(nums)
for i in range(len(nums)):
	if nums[i] < 0:
		continue
	else:
		nums.insert(i+1,nums[i]+1)
		break

print(nums)
