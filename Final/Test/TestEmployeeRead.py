from Final.Test.TestEmployeeWrite import employee
from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.employee import Employee

jff=JsonFileFactory()
filename= "../dataset/employees.json"
employees=jff.read_data(filename,Employee)
print("Danh sách Employee sau khi đọc file:")
for e in employee:
    print(e)