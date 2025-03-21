from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.manager import Manager

managers=[]
managers.append(Manager("01","Bob  ","bob  ","123"))
managers.append(Manager("02","Sally","sally","456"))
managers.append(Manager("03","Kevin","kevin","789"))
print("Danh sách Managers:")
for m in managers:
    print(m)
jff=JsonFileFactory()
filename= "../dataset/managers.json"
jff.write_data(managers,filename)

