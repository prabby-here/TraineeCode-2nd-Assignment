from salary_calculator import SalaryCalculator


class Employee:
    """
    Properties of the class
    """
    def __init__(self, emp_id, name, basic, hra, allowance_percentage, role):
        self.emp_id = emp_id
        self.name = name
        self.basic = float(basic)
        self.hra = float(hra)
        self.allowance_percentage = float(allowance_percentage)
        self.role = int(role)

    def get_salary(self):
        return SalaryCalculator.get_salary(self)

    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)
