import pandas as pd
import numpy as np

# 1. Tạo bảng dữ liệu Sinh Viên
data_sv = {
    "MaSV": ["SV01", "SV02", "SV03", "SV04", "SV05", "SV06", "SV07", "SV08", "SV09", "SV10"],
    "HoTen": ["Nguyen Van A", "Tran Thi B", "Le Van C", "Pham Thi D", "Hoang Van E",
              "Do Thi F", "Bui Van G", "Nguyen Thi H", "Tran Van I", "Le Thi K"],
    "Lop": ["CNTT1", "CNTT1", "CNTT2", "CNTT2", "CNTT1",
            "CNTT3", "CNTT3", "CNTT2", "CNTT1", "CNTT3"],
    "DiemPython": [8.5, 7.0, np.nan, 6.0, 9.0, 5.5, 7.5, np.nan, 4.5, 8.0],
    "DiemWeb": [7.5, np.nan, 6.5, 8.0, 9.0, 5.0, np.nan, 7.0, 4.0, 8.5],
    "DiemDatabase": [8.0, 6.5, 7.0, np.nan, 8.5, 5.0, 7.0, 6.5, np.nan, 9.0]
}

df_sv = pd.DataFrame(data_sv)

print("=== BẢNG DỮ LIỆU SINH VIÊN BAN ĐẦU ===")
print(df_sv)

# Lưu ra file CSV để thực hiện yêu cầu đọc file
df_sv.to_csv("sinhvien.csv", index=False, encoding="utf-8-sig")

# 2. Đọc file và kiểm tra dữ liệu null
df = pd.read_csv("sinhvien.csv")

print("\n=== KIỂM TRA DỮ LIỆU NULL ===")
print(df.isnull())

print("\n=== SỐ LƯỢNG GIÁ TRỊ NULL MỖI CỘT ===")
print(df.isnull().sum())

# 3. Điền giá trị null bằng 0
df = df.fillna(0)

print("\n=== DỮ LIỆU SAU KHI ĐIỀN NULL = 0 ===")
print(df)

# 4. Tạo cột DiemTB = trung bình 3 môn
df["DiemTB"] = (df["DiemPython"] + df["DiemWeb"] + df["DiemDatabase"]) / 3

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

df["XepLoai"] = df["DiemTB"].apply(xep_loai)

print("\n=== DỮ LIỆU SAU KHI THÊM DiemTB VÀ XepLoai ===")
print(df)

# 6. Thống kê dữ liệu theo cột Lop
print("\n=== THỐNG KÊ SỐ LƯỢNG SINH VIÊN THEO LỚP ===")
thong_ke_lop = df.groupby("Lop").size()
print(thong_ke_lop)

# 7. Tính điểm trung bình DiemTB của mỗi lớp
print("\n=== ĐIỂM TRUNG BÌNH DiemTB CỦA MỖI LỚP ===")
diemtb_moi_lop = df.groupby("Lop")["DiemTB"].mean()
print(diemtb_moi_lop)

# 8. Tạo bảng Thông Tin Lớp
data_lop = {
    "Lop": ["CNTT1", "CNTT2", "CNTT3"],
    "GiaoVien": ["Thay Nam", "Co Lan", "Thay Hung"],
    "PhongHoc": ["P101", "P102", "P103"]
}

df_lop = pd.DataFrame(data_lop)

print("\n=== BẢNG THÔNG TIN LỚP ===")
print(df_lop)

# 9. Ghép bảng Sinh Viên với bảng Thông Tin Lớp theo cột Lop
df_ghep = pd.merge(df, df_lop, on="Lop", how="left")

print("\n=== BẢNG GHÉP SINH VIÊN VÀ THÔNG TIN LỚP ===")
print(df_ghep)