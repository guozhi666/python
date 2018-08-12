lists = [5, 4, 3, 2, 1]
def arr(lists):
	#选择排序
	count = len(lists)
	for i in range(0, count - 1):
		t = i
		for j in range(i + 1, count):
			
			if lists[i] > lists[j]:
				t = j
			lists[t], lists[i] = lists[i], lists[t]
	return lists
print(arr(lists))