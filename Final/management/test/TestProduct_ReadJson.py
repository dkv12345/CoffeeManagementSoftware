from Final.management.libs.JsonFileFactory import JsonFileFactory
from Final.management.models import Product

jff=JsonFileFactory()
filename=r"D:\Final (4)\management\dataset\Product.json"
products=jff.read_data(filename,Product)
print("List of Products from Json:")
for p in products:
    print(p)