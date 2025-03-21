# Tạo 3 đối tượng Employee giả lập
from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.customer import Customer

customer= []
customer.append(Customer("1", "John Smith     ", "1234567890","Normal"))
customer.append(Customer("2", "Emma Johnson   ", "0987654321",  "VIP"))
customer.append(Customer("3","Michael Brown   ","1122334455","Normal"))
customer.append(Customer("3", "Sophia Martinez ", "2233445566","VIP"))
customer.append(Customer("4","William Anderson ","3344556677","Normal"))
print("Danh sách Customers:")
for c in customer:
    print(c)
jff=JsonFileFactory()
filename= "../dataset/customer.json"
jff.write_data(customer,filename)