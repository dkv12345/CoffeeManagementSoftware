from Final.management.libs.DataConnector import DataConnector

dc=DataConnector()
#read all products:
products=dc.get_all_products()
print("List of Products in database:")
for p in products:
    print(p)