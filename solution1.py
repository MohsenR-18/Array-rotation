def rotate(arr, d):
    new_arr = arr[d:] + arr[:d]

    print(new_arr)

m_array = [1, 2, 3, 4, 5, 6, 7]
d = 2
rotate(m_array, d)
