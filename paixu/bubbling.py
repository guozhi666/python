lists = [5, 4, 3, 2, 1]
def arr(lists):
	#冒泡排序
	count = len(lists)
	for i in range(0, count-1):
		for j in range(count-1, i+1,-1):
			if lists[i] > lists[j]:
				lists[i], lists[j] = lists[j], lists[i]
	return lists
print (arr(lists))