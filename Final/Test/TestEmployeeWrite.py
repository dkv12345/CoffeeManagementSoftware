from Final.models.JsonFileFactory import JsonFileFactory
from Final.models.employee import Employee
employee= [Employee(101, "Alice Johnson", "alice", "pass123"), Employee(102, "Smith Anderson", "smith", "pass456"),
           Employee(103, "Charles Nguyen", "charles", "pass789")]
print("Danh sách Employee:")
for e in employee:
    print(e)
jff=JsonFileFactory()
filename= "../dataset/employees.json"
jff.write_data(employee,filename)