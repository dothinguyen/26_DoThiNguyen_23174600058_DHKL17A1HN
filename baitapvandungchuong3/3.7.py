import numpy as np

np_baseball = np.loadtxt('chuong3\\baseball_2D.txt', delimiter=',')


print("Dòng thứ 50 trong np_baseball:")
print(np_baseball[49])

print("\nChiều cao của các cầu thủ từ dòng 124 trở đi:")
print(np_baseball[123:, 0]) 


mean_height = np.mean(np_baseball[:, 0])  
print("\nChiều cao trung bình của các cầu thủ:")
print(mean_height)

correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])
print("\nHệ số tương quan giữa chiều cao và cân nặng:")
print(correlation[0, 1])