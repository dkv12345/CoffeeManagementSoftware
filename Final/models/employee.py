class Employee:
    def __init__(self, EmployeeId=None, EmployeeName= None, UserName=None, Password=None):
        self.EmployeeId=EmployeeId
        self.EmployeeName=EmployeeName
        self.UserName=UserName
        self.Password=Password
    def __str__(self):
        return f"{self.EmployeeId}\t{self.EmployeeName}\t{self.UserName}\t{self.Password}"
