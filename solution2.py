def rotate(arr, d):
    for i in range(d):
        arr.append(arr[i])

    for j in range(d):
        arr.remove(arr[0])

    print(arr)

m_array = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotate(m_array, d)
