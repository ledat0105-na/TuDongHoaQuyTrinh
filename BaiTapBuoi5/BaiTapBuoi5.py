from abc import ABC, abstractmethod

# 1. Class Employee
class Employee(ABC):
    def __init__(self, id, name, salary):
        self.id = id
        self.name = name
        self.__salary = salary  

    # Getter
    def get_salary(self):
        return self.__salary

    # Setter
    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Lương không hợp lệ!")

    # Hiển thị thông tin
    def display_info(self):
        print(f"ID: {self.id}")
        print(f"Tên: {self.name}")
        print(f"Lương cơ bản: {self.__salary}")

    # Phương thức trừu tượng
    @abstractmethod
    def calculate_salary(self):
        pass


# 2. Class Developer kế thừa từ Employee
class Developer(Employee):
    def __init__(self, id, name, salary, programming_language, overtime_hours):
        super().__init__(id, name, salary)
        self.programming_language = programming_language
        self.overtime_hours = overtime_hours

    def calculate_salary(self):
        return self.get_salary() + self.overtime_hours * 200

    def display_info(self):
        super().display_info()
        print(f"Ngôn ngữ lập trình: {self.programming_language}")
        print(f"Số giờ tăng ca: {self.overtime_hours}")
        print(f"Tổng lương: {self.calculate_salary()}")


# 3. Class Manager kế thừa từ Employee
class Manager(Employee):
    def __init__(self, id, name, salary, bonus):
        super().__init__(id, name, salary)
        self.bonus = bonus

    def calculate_salary(self):
        return self.get_salary() + self.bonus

    def display_info(self):
        super().display_info()
        print(f"Thưởng: {self.bonus}")
        print(f"Tổng lương: {self.calculate_salary()}")


# Tạo đối tượng Developer
dev1 = Developer("DEV01", "Nguyễn Văn A", 5000, "Python", 10)

# Tạo đối tượng Manager
mgr1 = Manager("MGR01", "Trần Thị B", 8000, 3000)

print("===== THÔNG TIN LẬP TRÌNH VIÊN =====")
dev1.display_info()

print("\n===== THÔNG TIN QUẢN LÝ =====")
mgr1.display_info()