test = [1,5,3,67,6,35,2,3,5,6,53]

def selection_sort(arr1):
    print(arr1)
    if len(arr1) == 0 or len(arr1) == 0:
        return arr1

    else:
        low = arr1.pop(arr1.index(min(arr1)))
        arr1.insert(0,low)
        arr1 = [arr1[0]] + selection_sort(arr1[1:])
    return arr1
        
test = selection_sort(test)
print(test)