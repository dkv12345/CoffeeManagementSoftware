from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.manager import Manager

jff=JsonFileFactory()
filename= "../dataset/managers.json"
manager=jff.read_data(filename,Manager)
print("Danh sách Managers sau khi đọc file:")
for m in manager:
    print(m)