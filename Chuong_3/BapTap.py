import pandas as pd

# 1. Tạo bảng dữ liệu Sinh Viên
data_sv = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05", "SV06", "SV07", "SV08", "SV09", "SV10"],
    "HoTen": ["An", "Bình", "Chi", "Dũng", "Em", "Phúc", "Giang", "Hà", "Khánh", "Linh"],
    "Lop": ["23CT1", "23CT2", "23CT1", "23CT2", "23CT3", "23CT1", "23CT3", "23CT2", "23CT1", "23CT3"],
    "DiemPython": [8.5, 7.0, None, 6.0, 9.0, 7.5, 5.0, None, 8.0, 6.5],
    "DiemWeb": [7.5, None, 8.0, 6.5, 9.5, 7.0, None, 5.5, 8.5, 6.0],
    "DiemDatabase": [8.0, 6.5, 7.5, None, 9.0, 8.0, 5.5, 6.0, None, 6.5]
}

df_sv = pd.DataFrame(data=data_sv)
print("1. ===== BẢNG DỮ LIỆU SINH VIÊN BAN ĐẦU =====")
print(df_sv)

print("------------------------------------------------------")

# 2. Đọc dữ liệu và kiểm tra null
print("2. ===== KIỂM TRA DỮ LIỆU NULL =====")
print(df_sv.isnull())
print("Số lượng giá trị null theo từng cột:")
print(df_sv.isnull().sum())

print("------------------------------------------------------")

# 3. Điền giá trị null bằng 0
df_sv.fillna(value=0, inplace=True)
print("3. ===== DỮ LIỆU SAU KHI ĐIỀN NULL = 0 =====")
print(df_sv)

print("------------------------------------------------------")

# 4. Tạo cột DiemTB = trung bình 3 môn
df_sv["DiemTB"] = (df_sv["DiemPython"] + df_sv["DiemWeb"] + df_sv["DiemDatabase"]) / 3
print("4. ===== BẢNG SAU KHI THÊM CỘT DiemTB =====")
print(df_sv)

print("------------------------------------------------------")

# 5. Tạo cột XepLoai
def xep_loai(diem):
    if diem >= 8:
        return "Giỏi"
    elif diem >= 6.5:
        return "Khá"
    elif diem >= 5:
        return "Trung bình"
    else:
        return "Yếu"

df_sv["XepLoai"] = df_sv["DiemTB"].apply(xep_loai)

print("5. ===== BẢNG SAU KHI THÊM CỘT XepLoai =====")
print(df_sv)

print("------------------------------------------------------")


