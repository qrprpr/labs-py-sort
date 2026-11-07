def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Построение максимальной кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    print("Построенная куча:", arr)

    # Извлечение максимальных элементов
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]

        heapify(arr, i, 0)

        extraction = n - i

        if extraction <= 2:
            print(f"После извлечения {extraction}:")
            print("Куча:", arr[:i])
            print("Весь список:", arr)

    return arr


T1 = [5, 3, 8, 4, 2, 7, 1, 6]

print("Исходный список:", T1)
print("Отсортированный список:", heap_sort(T1.copy()))