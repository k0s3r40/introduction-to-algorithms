def insert_sort(arr, reverse=False):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        if reverse is False:
            while i >= 0 and arr[i] >= key:
                arr[i + 1] = arr[i]
                i -= 1
        else:
            while i >= 0 and arr[i] <= key:
                arr[i + 1] = arr[i]
                i -= 1
        arr[i + 1] = key
    return arr


if __name__ == '__main__':
    print("Increasing", insert_sort([100, 5, 1, 5, 6, 1, 5, 4, 6, 7, 8, 9, 0, 10]))
    print("Decreasing", insert_sort([100, 5, 1, 5, 6, 1, 5, 4, 6, 7, 8, 9, 0, 10], reverse=True))
