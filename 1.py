def bubble_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        swapped = False

        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if i < 2:
            print(f"После прохода {i + 1}: {arr}")

        if not swapped:
            break

    return arr


T1 = [5, 3, 8, 4, 2, 7, 1, 6]

print("Исходный список:", T1)
print("Отсортированный список:", bubble_sort(T1.copy()))