def insert_sort(arr):
    for j in range(1, len(arr)):
        key = arr[j]
        i = j - 1
        while i >= 0 and arr[i] >= key:
            arr[i + 1] = arr[i]
            i -= 1
        arr[i + 1] = key
        print(arr)


if __name__ == '__main__':
    arr = [100, 5, 1, 5, 6, 1, 5, 4, 6, 7, 8, 9, 0, 10]
    insert_sort(arr)
