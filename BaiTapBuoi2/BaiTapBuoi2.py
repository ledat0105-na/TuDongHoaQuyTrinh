
def print_separator():
    print("=" * 50)


class SimpleInterestAccount:
    """Lớp tính lãi đơn cho tài khoản tiết kiệm"""
    def __init__(self, principal, annual_rate, years):
        self.principal = principal          
        self.annual_rate = annual_rate     
        self.years = years               

    def calculate_interest(self, years=None):
        """Tính tiền lãi đơn"""
        if years is None:
            years = self.years
        return self.principal * self.annual_rate * years

    def total_amount(self, years=None):
        """Tính tổng tiền nhận được"""
        return self.principal + self.calculate_interest(years)

    def average_monthly_interest(self, years=None):
        """Tính tiền lãi trung bình mỗi tháng"""
        if years is None:
            years = self.years
        total_interest = self.calculate_interest(years)
        return total_interest / (years * 12)


if __name__ == "__main__":
    print_separator()
    print("CHƯƠNG TRÌNH TÍNH LÃI ĐƠN GỬI TIẾT KIỆM")
    print_separator()

    account = SimpleInterestAccount(100000000, 0.05, 5)

    # Câu 1: Tiền lãi sau 3 năm
    interest_3_years = account.calculate_interest(3)

    # Câu 2: Tổng tiền nhận được sau 5 năm
    total_5_years = account.total_amount(5)

    # Câu 3: Tiền lãi trung bình mỗi tháng trong 5 năm
    avg_monthly_interest = account.average_monthly_interest(5)

    print(f"1. Tiền lãi sau 3 năm (lãi đơn): {interest_3_years:,.0f} VND")
    print(f"2. Tổng tiền nhận được sau 5 năm: {total_5_years:,.0f} VND")
    print(f"3. Tiền lãi trung bình mỗi tháng: {avg_monthly_interest:,.0f} VND")

    print_separator()