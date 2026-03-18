import pandas
name = ["Alice", "Bob", "Charlie", "David", "Eva"]
data_series_name = pandas.Series(data=name, name="Name")
print(data_series_name)

age = [25, 30, 35, 40, 45]
data_series_age = pandas.Series(data=age, name="Age")
print(data_series_age)

