def selection_sort(arr):
    n = len(arr)

    for i in range(n - 1):
        min_index = i

        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        if i < 5:
            print(f"Шаг {i + 1}: индекс минимума = {min_index}")

        arr[i], arr[min_index] = arr[min_index], arr[i]

        if i < 5:
            print("Список после обмена:", arr)

    return arr


T1 = [5, 3, 8, 4, 2, 7, 1, 6]

print("Исходный список:", T1)
print("Отсортированный список:", selection_sort(T1.copy()))