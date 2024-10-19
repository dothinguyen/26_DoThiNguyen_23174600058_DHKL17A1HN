import numpy as np

heights_file = 'Bài 3.5\heights_file.txt'
weights_file = 'Bài 3.5\weights_file.txt'

with open(heights_file, 'r') as f_height:
    height = [float(line.strip()) for line in f_height]

with open(weights_file, 'r') as f_weight:
    weight = [float(line.strip()) for line in f_weight]
arr_height = np.array(height)
arr_weight = np.array(weight)

conversion_factor_height = 0.0254
arr_height_m = arr_height * conversion_factor_height

conversion_factor_weight = 0.453592
arr_weight_kg = arr_weight * conversion_factor_weight

arr_bmi = arr_weight_kg / (arr_height_m ** 2)

if len(arr_weight_kg) > 50:
    weight_at_index_50 = arr_weight_kg[50]
    print(f"Cân nặng ở vị trí index 50: {weight_at_index_50:.2f} kg")
else:
    print("Không có giá trị ở vị trí index 50.")

arr_height_m_100 = arr_height_m[100:111]  
print("Chiều cao (m) từ index 100 đến 110:", arr_height_m_100)

players_with_low_bmi = arr_bmi[arr_bmi < 21]
print("Các cầu thủ có BMI < 21:", players_with_low_bmi)

average_height = np.mean(arr_height_m)
average_weight = np.mean(arr_weight_kg)
print(f"Chiều cao trung bình: {average_height:.2f} m")
print(f"Cân nặng trung bình: {average_weight:.2f} kg")

max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print(f"Chiều cao lớn nhất: {max_height:.2f} m")
print(f"Cân nặng lớn nhất: {max_weight:.2f} kg")

min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print(f"Chiều cao nhỏ nhất: {min_height:.2f} m")
print(f"Cân nặng nhỏ nhất: {min_weight:.2f} kg")