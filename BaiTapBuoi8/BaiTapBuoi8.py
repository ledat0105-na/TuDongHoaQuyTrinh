import requests
from bs4 import BeautifulSoup
import pandas as pd

base_url = "http://books.toscrape.com/catalogue/page-{}.html"

du_lieu_sach = []

# 1. Lấy 5 trang đầu tiên
for page in range(1, 6):
    url = base_url.format(page)
    response = requests.get(url)
    response.encoding = "utf-8"

    soup = BeautifulSoup(response.text, "html.parser")

    # mỗi quyển sách nằm trong article class="product_pod"
    ds_sach = soup.find_all("article", class_="product_pod")

    for sach in ds_sach:
        # 2. Lấy thông tin: Tên sách
        ten_sach = sach.h3.a["title"]

        # Giá
        gia = sach.find("p", class_="price_color").text.strip()

        # Đánh giá
        danh_gia = sach.find("p", class_="star-rating")["class"][1]

        # Tình trạng
        tinh_trang = sach.find("p", class_="instock availability").text.strip()

        du_lieu_sach.append({
            "Tên sách": ten_sach,
            "Giá": gia,
            "Đánh giá": danh_gia,
            "Tình trạng": tinh_trang
        })

# Tạo DataFrame
df = pd.DataFrame(du_lieu_sach)

# 3. Xuất kết quả ra Excel với tên Sheet: Danh sách Sách
df.to_excel("danh_sach_sach.xlsx", sheet_name="Danh sách Sách", index=False)

print("Đã lấy dữ liệu thành công và xuất ra file danh_sach_sach.xlsx")
print(df.head())