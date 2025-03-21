from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.products import Product

products=[]
products.append(Product("01","Chocolate Balance","36","10"))
products.append(Product("02","Dark Chocolate   ","50","10"))
products.append(Product("03","Milk Chocolate   ","55","10"))
products.append(Product("04","Classical Cold Brew","38","10"))
products.append(Product("05","Vanilla Cold Brew ","40","10"))
products.append(Product("06","Medium Roast Blend","45","10"))
products.append(Product("07","Vanilla Roast     ","40","10"))
products.append(Product("08","Uji Matcha.       ","70","10"))
products.append(Product("09","Kyoto Matcha.     ","80","10"))
products.append(Product("10","Special Blend     ","35","10"))
products.append(Product("11","Dark Roast        ","45","10"))
products.append(Product("12","Light Roast       ","35","10"))
products.append(Product("13","Instant Coffee    ","30","10"))
products.append(Product("14","Mocha Coffee      ","30","10"))
print("Danh sách Products:")
for p in products:
    print(p)
jff=JsonFileFactory()
filename= "../dataset/products.json"
jff.write_data(products,filename)