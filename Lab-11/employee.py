from salary_calculator import SalaryCalculator
from role_builder import RoleBuilder


class Employee:
    """
    Properties of the class
    """
    def __init__(self, emp_id="", name="", basic=0.0, hra=0.0, allowance_percentage=0.0, role=0):
        self.emp_id = emp_id
        self.name = name
        self.basic = float(basic)
        self.hra = float(hra)
        self.allowance_percentage = float(allowance_percentage)
        # role can be int (id) or Roles enum
        try:
            # if it's numeric-like, store as int
            self.role = int(role)
        except (TypeError, ValueError):
            # otherwise keep as-is (e.g., Enum)
            self.role = role

    def get_salary(self):
        return SalaryCalculator.get_salary(self)

    def get_allowance(self):
        return SalaryCalculator.get_allowance(self)

    def get_role_description(self):
        return RoleBuilder.get_role_description(self.role)
