from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.customer import Customer

jff=JsonFileFactory()
filename= "../dataset/customer.json"
customer=jff.read_data(filename,Customer)
print("Danh sách Customers sau khi đọc file:")
for c in customer:
    print(c)