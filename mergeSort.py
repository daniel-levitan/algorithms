def merge(left, right, compare):

	result = []
	i, j = 0, 0 

	while i < len(left) and j < len(right):
		if compare(left[i], right[i]):
			result.append(left[i])
			i += 1
		else:
			result.append(right[i])
			j += 1

		while i < len(left):
			result.append(left[i])
			i += 1

		while j < len(right):
			result.append(right[j])
			j += 1

	return result


def mergeSort(list, compare = lambda x,y: x < y):
	if len(list) < 2:
		return list
	else:
		mid = len(list) // 2
		left = mergeSort(list[:mid], compare)
		right = mergeSort(list[mid:], compare)
		return merge(left, right, compare)


L = [2, 1, 4, 5, 3]
print(mergeSort(L))
print(mergeSort(L, lambda x,y: x > y))