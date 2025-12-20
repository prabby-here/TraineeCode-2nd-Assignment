"""
Class to represent employee information
"""
class Employee:
    def __init__(self, emp_id="", emp_name="", emp_gender="", address=None):
        self.emp_id = emp_id
        self.emp_name = emp_name
        self.emp_gender = emp_gender
        self.address = address