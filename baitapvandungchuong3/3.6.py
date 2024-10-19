print(arr_true)
#2
print("phần 2: ")
arr_1D = np.array([0,1,2,3,4,5,6,7,8])
arr_2D = arr_1D.reshape((3, 3))
print(arr_2D)
arr_2D = arr_2D[:,::-1]
print(arr_2D)
#3
print("phần 3: ")
arr_2D = arr_2D[::-1,:]
print(arr_2D)
#4
print("phần 4: ")
arr_2D = arr_2D[::-1,:]
print(arr_2D)
#5
print("phần 5: ")
arr_2D = arr_2D[:,::-1]
print(arr_2D)
#6
print("phần 6: ")
arr_2D_null = np.array([[1, 2, 3], [np.nan, 5, 6], [7, np.nan, 9], [4, 5, 6]])
print(arr_2D_null)
ktra_rong = np.isnan(arr_2D_null).any()
print(ktra_rong)
#7
print("phần 7: ")
arr_2D_null[np.isnan(arr_2D_null)] = 0
print(arr_2D_null)