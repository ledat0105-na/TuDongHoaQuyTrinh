# a = 3
# b = 2
# # Cộng
# c = a + b
# print(c)
# # Trừ
# d = a - b
# print(d)
# # Nhân
# e = a * b
# print(e)
# # Chia
# f = a / b
# print(f)
# # Chia lấy dư
# g = a % b
# print(g)
# # Chia lấy nguyên
# h = a // b
# print(h)
# # Lũy thừa
# k = a ** b
# print(k)

# Bạn có 2.000.000 đồng.
# Mua áo quần 1.000.000 đồng
# Mua đồ ăn 1.550.000 đồng
# Đi làm thêm được 3.000.000 đồng
# Số tiền còn lại là bao nhiêu?
# Yêu cầu: dùng toán tử gán rút gọn

# tien = 2_000_000      # Bạn có 2.000.000 đồng

# tien -= 1_000_000    # Mua áo quần
# tien -= 1_550_000    # Mua đồ ăn
# tien += 3_000_000    # Đi làm thêm

# print("Số tiền còn lại là:", tien, "đồng")

# number_one = 10
# number_two = 20
# result = number_one == number_two

# if number_one == number_two:
#     print(number_one==number_two)

# elif number_one != number_two:
#     print(number_one!=number_two)

# elif number_one > number_two:
#     print(number_one>number_two)

# elif number_one < number_two:
#     print(number_one<number_two)

# elif number_one >= number_two:
#     print(number_one>=number_two)

# elif number_one <= number_two:
#     print(number_one<=number_two)

#nhap vao 1 so nguyen kiem tra so chan hay le
# number=int(input("Nhập số nguyên: "))
  
# if number % 2 == 0:
#     print("Số chẵn")
# else :
#     print("Số lẻ")

diem_tb = int(input("Nhập điểm trung bình của bạn: "))
  
if diem_tb >= 8.5:
    print("Loại Giỏi")
elif diem_tb >= 6.5:
    print("Loại Khá")
elif diem_tb >= 5:
    print("Loại Trung bình")
elif diem_tb < 5:
    print("Loại Yếu")