def array_filtering(array, array_date):
    i = 1
    while i < len(array)-1:
        if array[i-1] < array[i] < array[i+1] or array[i-1] == array[i] or array[i-1] > array[i] > array[i+1]:
            array.pop(i)
            array_date.pop(i)
        else: i += 1
    return array

def profit(array, bool, reverse, logging):
    FIAT = ['RUR', 'USD']
    if reverse: i = int(bool)
    else: i = int(not bool)
    fiat = 1
    while i < len(array) - 1:
        if logging:
            print('%s%s' % (date_array[i + int(bool)], FIAT[int(bool)]))
            print('%s%s' % (date_array[i + int(not bool)], FIAT[int(not bool)]))
        else:
            fiat *= array[i + int(bool)]
            fiat /= array[i + int(not bool)]
        i += 2
    return (fiat - 1)*100

def print_result(array):
    if array[0] > array[1]:
        usd = profit(array, False, True, False)
        rur = profit(array, True, True, False)
        if usd < rur: #USD < RUR and ascending array
            print('Начинаем с RUR')
            profit(array, True, True, True)
            print("Прибыль: %d%%" % rur)
        else:
            print("Начинаем с USD")
            profit(array, False, True, True)
            print("Прибыль: %d%%" % usd)
    else:
        rur = profit(array, False, False, False)
        usd = profit(array, True, False, False)
        if usd < rur: #USD < RUR and descending array
            print('Начинаем с USD')
            profit(array, False, False, True)
            print("Прибыль: %d%%" % rur)
        else:
            print("Начинаем с RUR")
            profit(array, True, False, True)
            print("Прибыль: %d%%" % usd)

if __name__ == '__main__':
    date_array, array_currencies = [], []
    line = ['','']
    try:
        while line[0] != 'quit':
            line = input().split('-')
            if line[0] != 'quit':
                date_array.append(line[0])
                array_currencies.append(float(line[1]))
        print_result(array_filtering(array_currencies, date_array))
    except:
        print("ERROR INPUT")
    

