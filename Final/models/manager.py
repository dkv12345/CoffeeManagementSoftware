class Manager:
    def __init__(self, ManagerID=None, ManagerName=None, ManagerUsername=None, ManagerPassword = None):
        self.ManagerID = ManagerID
        self.ManagerName = ManagerName
        self.ManagerUsername = ManagerUsername
        self.ManagerPassword = ManagerPassword

    def __str__(self):
        return f"{self.ManagerID}\t{self.ManagerName}\t{self.ManagerUsername}\t{self.ManagerPassword}"
