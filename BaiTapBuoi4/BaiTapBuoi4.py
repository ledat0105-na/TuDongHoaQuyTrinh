import math

# Bài 1: Giải phương trình bậc 2
print("BÀI 1: GIẢI PHƯƠNG TRÌNH BẬC 2")
a = float(input("Nhập a = "))
b = float(input("Nhập b = "))
c = float(input("Nhập c = "))

if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm")
        else:
            print("Phương trình vô nghiệm")
    else:
        x = -c / b
        print("Phương trình bậc nhất có nghiệm x =", x)
else:
    delta = b**2 - 4*a*c
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x1 =", x1)
        print("x2 =", x2)
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép x =", x)
    else:
        print("Phương trình vô nghiệm")

# Bài 2: Bảng cửu chương từ 2 đến 9
print("\nBÀI 2: BẢNG CỬU CHƯƠNG TỪ 2 ĐẾN 9")
for i in range(2, 10):
    print(f"\nBảng cửu chương {i}:")
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")

# Bài 3: Tổng các số chẵn từ 1 đến 100
print("\nBÀI 3: TÍNH TỔNG CÁC SỐ CHẴN TỪ 1 ĐẾN 100")
tong = 0
for i in range(1, 101):
    if i % 2 == 0:
        tong += i
print("Tổng các số chẵn từ 1 đến 100 là:", tong)

# Bài 4: Kiểm tra số nguyên tố
print("\nBÀI 4: KIỂM TRA SỐ NGUYÊN TỐ")
n = int(input("Nhập số nguyên n = "))
if n < 2:
    print(n, "không phải là số nguyên tố")
else:
    la_so_nguyen_to = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            la_so_nguyen_to = False
            break
    if la_so_nguyen_to:
        print(n, "là số nguyên tố")
    else:
        print(n, "không phải là số nguyên tố")

# Bài 5: In hình tam giác
print("\nBÀI 5: IN HÌNH TAM GIÁC")
h = int(input("Nhập chiều cao tam giác h = "))
for i in range(1, h + 1):
    print("*" * i)

# Bài 6: Tìm ƯCLN và BCNN
print("\nBÀI 6: TÌM ƯCLN VÀ BCNN")
a = int(input("Nhập số a = "))
b = int(input("Nhập số b = "))

x = abs(a)
y = abs(b)

while y != 0:
    x, y = y, x % y

ucln = x

if a == 0 or b == 0:
    bcnn = 0
else:
    bcnn = abs(a * b) // ucln

print("ƯCLN =", ucln)
print("BCNN =", bcnn)

# Bài 7: Đếm số lượng chữ số của một số nguyên
print("\nBÀI 7: ĐẾM SỐ LƯỢNG CHỮ SỐ")
n = int(input("Nhập số nguyên n = "))
n = abs(n)

if n == 0:
    dem = 1
else:
    dem = 0
    while n > 0:
        dem += 1
        n //= 10

print("Số lượng chữ số là:", dem)