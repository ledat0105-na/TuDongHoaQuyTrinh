# 1. Nhập họ tên, tuổi, điểm trung bình và in ra màn hình
print("\nBài 1: Nhập thông tin sinh viên:")
ho_ten = input("Nhập họ tên: ")
tuoi = int(input("Nhập tuổi: "))
diem_tb = float(input("Nhập điểm trung bình: "))

print("\n--- Thông tin sinh viên ---")
print("Họ tên:", ho_ten)
print("Tuổi:", tuoi)
print("Điểm trung bình:", diem_tb)


# 2. Tính diện tích và chu vi hình chữ nhật
print("\nBài 2: Tính diện tích và chu vi hình chữ nhật:")
chieu_dai = float(input("\nNhập chiều dài: "))
chieu_rong = float(input("Nhập chiều rộng: "))

dien_tich = chieu_dai * chieu_rong
chu_vi = 2 * (chieu_dai + chieu_rong)

print("\n--- Hình chữ nhật ---")
print("Diện tích:", dien_tich)
print("Chu vi:", chu_vi)


# 3. Chuyển đổi nhiệt độ từ C sang F
print("\nBài 3: Chuyển đổi nhiệt độ từ C sang F")
do_c = float(input("\nNhập nhiệt độ C: "))
do_f = (do_c * 9 / 5) + 32

print("\n--- Chuyển đổi nhiệt độ ---")
print(do_c, "độ C =", do_f, "độ F")


# 4. Kiểm tra số chẵn hay lẻ
print("\nBài 4: Kiểm tra số chẵn hay lẻ")
so_nguyen = int(input("\nNhập một số nguyên: "))

if so_nguyen % 2 == 0:
    print(so_nguyen, "là số chẵn")
else:
    print(so_nguyen, "là số lẻ")


# 5. Tính tổng, hiệu, thương của hai số thực
print("\nBài 5: Tính tổng, hiệu, thương của hai số thực")
a = float(input("\nNhập số thực thứ nhất: "))
b = float(input("Nhập số thực thứ hai: "))

tong = a + b
hieu = a - b

print("\n--- Kết quả phép tính ---")
print("Tổng =", tong)
print("Hiệu =", hieu)

if b != 0:
    thuong = a / b
    print("Thương =", thuong)
else:
    print("Không thể tính thương vì số thứ hai bằng 0")