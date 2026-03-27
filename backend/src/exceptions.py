class DatabaseException(Exception):
    def __init__(self, detail: str = "Could not perform database operation"):
        self.detail = detail

class EmailExistsException(Exception):
    def __init__(self, detail: str = "Employee with this email already exists"):
        self.detail = detail