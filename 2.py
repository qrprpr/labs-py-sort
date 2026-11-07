def insertion_sort(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

        if i <= 3:
            print(f"После вставки {i}: {arr}")

    return arr


T1 = [5, 3, 8, 4, 2, 7, 1, 6]

print("Исходный список:", T1)
print("Отсортированный список:", insertion_sort(T1.copy()))