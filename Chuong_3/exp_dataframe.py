import pandas as pd

data_dict={
    "Name": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "Class": ["23CT1", "23CT2", "23CT1", "23CT2", "23CT1"],
    "DiemTb": [8.5, 7.0, 9.0, 6.5, 8.0],
    "Age": [25, 30, 35, 40, 45],
    "Address": ["Hanoi", "HCM", "Danang", "Hue", "Cantho"]
}

df_input=pd.DataFrame(data=data_dict)
print(df_input)

print("------------------------------------------------------")
#truy suat cot ten
print(df_input["Name"])
# truy suat cot diem
print(df_input["DiemTb"])
# truy suat row thu 2
print(df_input.iloc[1])
#lay ra gia tri trong o = index, ten cot
print(df_input.at[2, "DiemTb"])
#lay ra gia tri cuoi cung DiemTb dong cuoic cung
print(df_input["DiemTb"].iloc[-1])

# lọc dữ liệu
# lọc ra những học sinh có điểm trung bình >= 8.0 và lớp 23CT1
df_filtered_point_class = df_input[(df_input["DiemTb"] >= 8.0) & (df_input["Class"] == "23CT1")]
print(df_filtered_point_class)


my_var = None
my_str = " "
my_name = "Alice"
print(my_var)

# Xóa dữ liệu dòng trống: NaN
print(df_input.dropna())
print()

# điền dữ liệu vào dòng trống
df_input.fillna(value={"DiemTb": 7.0}, inplace=True)
print(df_input)

