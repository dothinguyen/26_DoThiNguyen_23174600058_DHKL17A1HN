import numpy as np

# Đọc dữ liệu từ tệp euro2012.csv
data = np.genfromtxt('chuong3\\euro2012.csv', delimiter=',', dtype=str, skip_header=1)

# Lấy các cột liên quan: Đội, Thẻ vàng, Thẻ đỏ
teams = data[:, 0]  # Cột tên đội bóng
yellow_cards = data[:, 1].astype(int)  # Cột thẻ vàng
red_cards = data[:, 2].astype(int)  # Cột thẻ đỏ

# 1. Danh sách các đội tham gia Euro 2012
print("Danh sách các đội tham gia Euro 2012:")
print(teams)

# 2. Số thẻ vàng của mỗi đội
print("\nSố thẻ vàng của mỗi đội:")
for team, yellow in zip(teams, yellow_cards):
    print(f"{team}: {yellow}")

# 3. Số thẻ đỏ của mỗi đội
print("\nSố thẻ đỏ của mỗi đội:")
for team, red in zip(teams, red_cards):
    print(f"{team}: {red}")

# 4. Sắp xếp theo số thẻ vàng tăng dần
sorted_indices_yellow = np.argsort(yellow_cards)  # Sắp xếp chỉ số theo thẻ vàng tăng dần
sorted_teams_yellow = teams[sorted_indices_yellow]  # Lấy tên đội theo thứ tự sắp xếp thẻ vàng
sorted_yellow_cards = yellow_cards[sorted_indices_yellow]  # Số thẻ vàng đã sắp xếp

print("\nDanh sách các đội sắp xếp theo số thẻ vàng (tăng dần):")
for team, yellow in zip(sorted_teams_yellow, sorted_yellow_cards):
    print(f"{team}: {yellow}")

# 5. Sắp xếp theo số thẻ đỏ tăng dần
sorted_indices_red = np.argsort(red_cards)  # Sắp xếp chỉ số theo thẻ đỏ tăng dần
sorted_teams_red = teams[sorted_indices_red]  # Lấy tên đội theo thứ tự sắp xếp thẻ đỏ
sorted_red_cards = red_cards[sorted_indices_red]  # Số thẻ đỏ đã sắp xếp

print("\nDanh sách các đội sắp xếp theo số thẻ đỏ (tăng dần):")
for team, red in zip(sorted_teams_red, sorted_red_cards):
    print(f"{team}: {red}")