def binarySearch(list, low, high, item):
	if high >= low:
		mid =  (high + low) // 2
		if list[mid] == item:
			return mid
		elif list[mid] > item:
			return binarySearch(list, low, mid-1, item)
		else:
			return binarySearch(list, mid+1, high, item)
	else:
		return None




my_list = [1, 3, 5, 7, 9]
print(binarySearch(my_list, 0, len(my_list)-1, 9))