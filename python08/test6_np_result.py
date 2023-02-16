import numpy as np

# arr_a = np.array([2,4,6])
# arr_b = np.array([3,5,7])
# print('배열 a :',arr_a)
# print('배열 b :',arr_b)
# arr_c = arr_a + arr_b
# print('배열 c :',arr_c)
# arr_c = np.zeros(3) # 초기값 0으로 다시 세팅
# print('초기화된 배열 c :',arr_c)
# print('배열 c의 타입 :',arr_c.dtype)

arr2_a = np.array([
    [2,4,6],
    [8,10,12],
    [14,16,18]
])

arr2_b = np.array([
    [1,3,5],
    [7,9,11],
    [13,15,17]
])

# print('배열 a :', '\n', arr2_a)
# print('배열 b :', '\n', arr2_b)
# print('배열 a + b :', '\n', arr2_a + arr2_b)
arr2_c = arr2_a + arr2_b
arr2_c = np.zeros((3,3))
print(arr2_c)