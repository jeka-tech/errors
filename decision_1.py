
# ниже количество едениц и нулей в массиве при каждой смене от 1 к 0 или наоборот
sourceList = [2, 1, 1, 4, 1, 2, 5, 2, 1, 1, 4, 1, 2, 1, 4, 2, 1, 1, 4, 1, 1]
bitList = []  # список, который мы генерируем

startBit = 1  # стартовое значение 1 или 0

for i in sourceList:                # для каждого элемента в sourceList
    for j in range (0, i):
        bitList.append(startBit)    # добавляем startBit в список столько раз, сколько указано в sourceList

    if startBit == 1:               # меняем startBit на противоположное значение
        startBit = 0
    else:
        startBit = 1

print(bitList)
