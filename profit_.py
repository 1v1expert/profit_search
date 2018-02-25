def change_array(array):
    i = 1
    while i < len(array)-1:
        if array[i-1] < array[i] < array[i+1] or array[i-1] == array[i] or array[i-1] > array[i] > array[i+1]:
            array.pop(i)
        i += 1
    print(array)
    return array

def procent(array, bool, reverse, logging):
    FIAT = ['RUR', 'USD']
    if reverse: i = int(bool)
    else: i = int(not bool)
    fiat = 1
    while i < len(array) - 1:
        if logging:
            print(array[i + int(bool)], FIAT[int(bool)])
            print(array[i + int(not bool)], FIAT[int(not bool)])
        else:
            fiat *= array[i + int(bool)]
            fiat /= array[i + int(not bool)]
            print(array[i + int(bool)], array[i + int(not bool)])
        i += 2
    return (fiat - 1)*100
def print_array(array, reverse):
    if reverse:
        usd = procent(array, False, reverse, False)
        rur = procent(array, True, reverse, False)
        if usd < rur: #USD < RUR
            print('Начинаем с RUR')
            procent(array, True, reverse, True)
            print("Прибыль: ", rur)
        else:
            print("Начинаем с USD")
            procent(array, False, reverse, True)
            print("Прибыль: ", usd)
    else:
        rur = procent(array, False, reverse, False)
        usd = procent(array, True, reverse, False)
        if usd < rur: #USD < RUR
            print('Начинаем с USD')
            procent(array, False, reverse, True)
            print("Прибыль: ", rur)
        else:
            print("Начинаем с RUR")
            procent(array, True, reverse, True)
            print("Прибыль: ", usd)

def iterable(array):
    if array[0] > array[1]:print_array(array, True)
    else: print_array(array, False)


if __name__ == '__main__':
    A = [60, 61, 62, 58, 58, 63, 57.5]
    B = [65, 60, 70, 62]
    C = [70, 75, 72, 76, 69]
    D = [70, 69]
    new_array = change_array(D)
    iterable(new_array)

