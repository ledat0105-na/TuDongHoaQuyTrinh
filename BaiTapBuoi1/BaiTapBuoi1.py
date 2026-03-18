def print_separator():
    print("=" * 60)


class Invoice:
    """Lớp đại diện cho một hóa đơn điện tử"""
    def __init__(self, supplier_name, invoice_date, amount, file_name):
        self.supplier_name = supplier_name
        self.invoice_date = invoice_date
        self.amount = amount
        self.file_name = file_name

    def is_valid(self):
        """Kiểm tra hóa đơn có đủ thông tin hay không"""
        return all([
            self.supplier_name,
            self.invoice_date,
            self.amount > 0,
            self.file_name
        ])

    def __str__(self):
        return (f"Hóa đơn: {self.file_name} | "
                f"Nhà cung cấp: {self.supplier_name} | "
                f"Ngày: {self.invoice_date} | "
                f"Số tiền: {self.amount:,} VND")


class SharedFolder:
    """Lớp mô phỏng thư mục dùng chung để lưu hóa đơn"""
    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.saved_files = []

    def save_invoice(self, invoice):
        if not invoice.is_valid():
            raise ValueError(f"Không thể lưu {invoice.file_name} vì hóa đơn thiếu thông tin.")
        self.saved_files.append(invoice.file_name)
        print(f"Đã lưu file '{invoice.file_name}' vào thư mục dùng chung: {self.folder_name}")

    def show_saved_files(self):
        print(f"Danh sách file trong thư mục '{self.folder_name}':")
        for idx, file in enumerate(self.saved_files, start=1):
            print(f"{idx}. {file}")


class EmailNotifier:
    """Lớp mô phỏng chức năng gửi email thông báo"""
    def __init__(self, manager_email):
        self.manager_email = manager_email

    def send_notification(self, total_files):
        print(f"Gửi email đến quản lý: {self.manager_email}")
        print(f"Nội dung: Đã tải thành công {total_files} hóa đơn về thư mục dùng chung.")


class RPABot:
    """Lớp bot RPA thực hiện quy trình tự động"""
    def __init__(self, bot_name, website_url, shared_folder, email_notifier):
        self.bot_name = bot_name
        self.website_url = website_url
        self.shared_folder = shared_folder
        self.email_notifier = email_notifier
        self.downloaded_invoices = []

    def open_website(self):
        print(f"{self.bot_name}: Đang mở website hóa đơn điện tử: {self.website_url}")

    def download_invoices(self, invoices):
        print(f"{self.bot_name}: Bắt đầu tải các file hóa đơn đính kèm...")
        for invoice in invoices:
            print(f"{self.bot_name}: Đã tải file {invoice.file_name}")
            self.downloaded_invoices.append(invoice)

    def check_invoice_info(self, invoice):
        print(f"{self.bot_name}: Kiểm tra thông tin hóa đơn {invoice.file_name}")
        print(f"  - Tên nhà cung cấp: {invoice.supplier_name}")
        print(f"  - Ngày hóa đơn: {invoice.invoice_date}")
        print(f"  - Số tiền: {invoice.amount:,} VND")

        if invoice.is_valid():
            print(f"{self.bot_name}: Hóa đơn hợp lệ")
            return True
        else:
            print(f"{self.bot_name}: Hóa đơn không hợp lệ")
            return False

    def save_valid_invoices(self):
        print(f"{self.bot_name}: Lưu các hóa đơn hợp lệ vào thư mục dùng chung...")
        valid_count = 0
        for invoice in self.downloaded_invoices:
            if self.check_invoice_info(invoice):
                self.shared_folder.save_invoice(invoice)
                valid_count += 1
            else:
                print(f"{self.bot_name}: Bỏ qua file {invoice.file_name} do thiếu thông tin")
        return valid_count

    def send_email_report(self, total_valid_files):
        self.email_notifier.send_notification(total_valid_files)

    def run_daily_process(self, invoices):
        print_separator()
        print(f"HỆ THỐNG RPA: {self.bot_name}")
        print_separator()

        self.open_website()
        print_separator()

        self.download_invoices(invoices)
        print_separator()

        total_valid_files = self.save_valid_invoices()
        print_separator()

        self.send_email_report(total_valid_files)
        print_separator()

        print(f"{self.bot_name}: Hoàn thành quy trình tự động tải hóa đơn.")


if __name__ == "__main__":
    shared_folder = SharedFolder("ThuMucHoaDon_DungChung")
    notifier = EmailNotifier("quanly@congty.com")

    bot = RPABot(
        bot_name="InvoiceBot",
        website_url="https://hoadon.example.com",
        shared_folder=shared_folder,
        email_notifier=notifier
    )

    invoices = [
        Invoice("Công ty ABC", "18/03/2026", 2500000, "HD001.pdf"),
        Invoice("Công ty XYZ", "18/03/2026", 3200000, "HD002.pdf"),
        Invoice("Công ty Minh An", "17/03/2026", 1800000, "HD003.pdf"),
        Invoice("", "17/03/2026", 1500000, "HD004.pdf") 
    ]

    bot.run_daily_process(invoices)

    print("Danh sách file đã lưu:")
    shared_folder.show_saved_files()