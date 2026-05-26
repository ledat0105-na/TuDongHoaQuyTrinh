import io
import os
from datetime import datetime
from bs4 import BeautifulSoup
import pandas as pd
import requests

URL = "https://giavang.org"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

SAVE_DIR = r"D:\DU LIEU\TUDONGHOAQUYTRINH\TuDongHoaQuyTrinh\BaiTapBuoi14"


def crawl_gia_vang():
    print("Bot đang kết nối tới website giavang.org...")

    try:
        response = requests.get(URL, headers=HEADERS, timeout=10)

        if response.status_code != 200:
            print(f"Không thể truy cập website. Mã lỗi: {response.status_code}")
            return

        soup = BeautifulSoup(response.content, "html.parser")
        tables = soup.find_all("table")

        if not tables:
            print("Không tìm thấy bảng dữ liệu nào trên website!")
            return

        print(f"Tìm thấy {len(tables)} bảng dữ liệu. Đang xử lý bảng đầu tiên...")
        target_table = tables[0]

        html_signal = io.StringIO(str(target_table))
        df_list = pd.read_html(html_signal)

        if df_list:
            df = df_list[0]

            current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
            file_name = f"bang_gia_vang_{current_time}.xlsx"

            if not os.path.exists(SAVE_DIR):
                os.makedirs(SAVE_DIR)
            full_file_path = os.path.join(SAVE_DIR, file_name)

            df.to_excel(full_file_path, index=False)
            print(f"Đã lưu dữ liệu thành công!")
            print(f"Vị trí file: {full_file_path}")
            print("\nXem trước dữ liệu vừa lưu:")
            print(df.head())
        else:
            print("Không thể chuyển đổi bảng thành dữ liệu Excel.")

    except Exception as e:
        print(f"Có lỗi xảy ra trong quá trình chạy bot: {e}")


if __name__ == "__main__":
    crawl_gia_vang()