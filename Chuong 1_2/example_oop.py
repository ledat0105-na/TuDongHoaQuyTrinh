class Car:
    def __init__(self, name, style, speed, color):
        self.name = name
        self.style = style
        self.speed = speed
        self.color = color

    def display_info(self):
        print(f"{self.name} {self.style} {self.speed} {self.color}")
car1 = Car("Toyota", "Sport", "50km/h", "Trang")
car2 = Car("Honda", "Nhỏ", "100km/h", "Do")
car1.display_info()  
car2.display_info()  


class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def display_info(self):
        print(f"{self.name} {self.age} {self.city}")
person1 = Person("Hai", 22, "Hà Nội")
person2 = Person("Dat", 18, "Nghệ An")
person1.display_info()
person2.display_info()

# Tạo class Employee với:
# Thuộc tính public: name, email, address
# Thuộc tính private: __name, __phone,  __base_salary
# Phương thức: get_info(), get_salary(), set_salary()
# Yêu cầu:
# Không được truy cập trực tiếp __base_salary
# Lương không được nhỏ hơn 0
class Employee:
    def __init__(self, name, email, address, phone, base_salary):
        self.name = name
        self.email = email
        self.address = address
        self.__phone = phone
        self.__base_salary = base_salary

    def get_info(self):
        print(f"Name: {self.name}, Email: {self.email}, Address: {self.address}")

    def get_salary(self):
        return self.__base_salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__base_salary = salary
        else:
            print("Lương không được nhỏ hơn 0")
employee1 = Employee("Hai", "hai@email.com", "Hà Nội", "123456789", 5000)
employee1.get_info()
print("Lương hiện tại:", employee1.get_salary())
employee1.set_salary(6000)
print("Lương sau khi cập nhật:", employee1.get_salary())
employee1.set_salary(-1000) 

# Kế thừa từ lớp cha sang lớp con 
# Thêm thuộc tính màu và phương thức (hành động) thay đổi màu
# Kế thừa, đóng gói
from abc import ABC, abstractmethod

class PersonABC(ABC):
    def __init__(self, name, salary):
        self.name = name
        # private attribute
        self.__salary = salary
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.__salary
    
    @abstractmethod
    def calculate_salary(self):
        pass


class EmployeeWithInheritance(PersonABC):
    def __init__(self, name, address, phone, salary):
        # Kế thừa thuộc tính name từ lớp Cha (PersonABC)
        super().__init__(name, salary)
        # Tạo các thuộc tính riêng cho Nhân viên
        self.address = address
        self.__phone = phone
    
    def get_info(self):
        print(f"Name: {self.get_name()}, Address: {self.address}")
    
    def get_phone(self):
        return self.__phone
    
    def calculate_salary(self):
        """Implement abstract method"""
        return self.get_salary()

# Class Developer: lương + thưởng kĩ thuật 20%
class Developer(EmployeeWithInheritance):
    def __init__(self, name, address, phone, salary):
        super().__init__(name, address, phone, salary)
    
    def calculate_salary(self):
        """Tính lương = lương cơ bản + thưởng kĩ thuật 20%"""
        base_salary = self.get_salary()
        bonus = base_salary * 0.2
        total_salary = base_salary + bonus
        print(f"\n[Developer: {self.get_name()}]")
        print(f"  Lương cơ bản: {base_salary:,.2f}")
        print(f"  Thưởng kĩ thuật (20%): {bonus:,.2f}")
        print(f"  Tổng lương: {total_salary:,.2f}")
        return total_salary


# Class Manager: lương + thưởng quản lý 30%
class Manager(EmployeeWithInheritance):
    def __init__(self, name, address, phone, salary):
        super().__init__(name, address, phone, salary)
    
    def calculate_salary(self):
        """Tính lương = lương cơ bản + thưởng quản lý 30%"""
        base_salary = self.get_salary()
        bonus = base_salary * 0.3
        total_salary = base_salary + bonus
        print(f"\n[Manager: {self.get_name()}]")
        print(f"  Lương cơ bản: {base_salary:,.2f}")
        print(f"  Thưởng quản lý (30%): {bonus:,.2f}")
        print(f"  Tổng lương: {total_salary:,.2f}")
        return total_salary


# Test kế thừa
print("=" * 50)
print("TEST KỾ THỪA EMPLOYEE")
print("=" * 50)
employee2 = EmployeeWithInheritance("Hoa", "TP Hồ Chí Minh", "987654321", 4500)
employee2.get_info()
print("Lương nhân viên:", employee2.calculate_salary())

print("\n" + "=" * 50)
print("TEST DEVELOPER (Lương + 20% thưởng kĩ thuật)")
print("=" * 50)
dev1 = Developer("Minh", "Hà Nội", "0987654321", 5000)
dev1.get_info()
print(f"Lương cơ bản: {dev1.get_salary()}")
print(f"Lương + thưởng 20%: {dev1.calculate_salary()}")

print("\n" + "=" * 50)
print("TEST MANAGER (Lương + 30% thưởng quản lý)")
print("=" * 50)
manager1 = Manager("Linh", "Đà Nẵng", "0912345678", 6000)
manager1.get_info()
print(f"Lương cơ bản: {manager1.get_salary()}")
print(f"Lương + thưởng 30%: {manager1.calculate_salary()}")