def change_array(array):
    i = 1
    while i < len(array)-1:
        if array[i-1] < array[i] < array[i+1] or array[i-1] == array[i] or array[i-1] > array[i] > array[i+1]:
            array.pop(i)
        i += 1
    print(array)
    return array



