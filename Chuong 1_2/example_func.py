# result_1 = 1 + 2
# result_2 = 10 + 2
# result_3 = 10 + 4
# result_4 = 1 + 6

# def tinh_tong(a,b):
#     result = a + b
#     return result
# result_1 = tinh_tong(10,2)
# print("Kết quả phép tính 1 của bạn là: ", result_1)

# result_2 = tinh_tong(10,4)
# print("Kết quả phép tính 2 của bạn là: ", result_2)   

# result_3 = tinh_tong(10,6)
# print("Kết quả phép tính 3 của bạn là: ", result_3)   

# result_4 = tinh_tong(10,8)
# print("Kết quả phép tính 4 của bạn là: ", result_4)   

#Viết hàm trả về danh sách số chẵn từ 1 đến 10
def Sochan():
    result = []
    for i in range(1, 11):
        if i % 2 == 0:
            result.append(i)
    return result

print("Danh sách số chẵn từ 1 đến 10 là: ", Sochan())



#Viết hàm trả về tổng số chẵn từ 1 đến 10
def Tong_Sochan():
    result = 0
    for i in range(1, 11):
        if i % 2 == 0:
            result += i
    return result

print("Tổng số chẵn từ 1 đến 10 là: ", Tong_Sochan())
