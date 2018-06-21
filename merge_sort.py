def merge_sort(arr1):
	if len(arr1) == 1:
		return arr1
	
	l = merge_sort(arr1[:len(arr1)//2])
	r = merge_sort(arr1[len(arr1)//2:])
	return merge(l,r)


def merge(arr1, arr2):
	arr3 = []
	i = j = 0
	while i < len(arr1) and j < len(arr2):
		if arr1[i] < arr2[j]:
			arr3.append(arr1[i])
			i += 1
		else:
			arr3.append(arr2[j])
			j += 1
	if i < len(arr1):
		arr3.extend(arr1[i:])
	else:
		arr3.extend(arr2[j:])
	return arr3