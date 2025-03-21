from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.products import Product

jff=JsonFileFactory()
filename= "../dataset/products.json"
product=jff.read_data(filename,Product)
print("Danh sách Products sau khi đọc file:")
for p in product:
    print(p)