from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
        # Employee array to hold the employees' information
        employees = [None] * 4
        emp = None

        emp_id = ""
        name = ""
        report_date = ""
        allowance_percentage = 0.0
        basic = 0.0
        hra = 0.0
        role = 0

        # Accept employee information from the user
        print("Enter employee information")

        for i in range(len(employees)):
            print("Employee No : " + str(i+1))
            print("Id : ")
            emp_id = input()

            print("Name : ")
            name = input()

            print("Basic : ")
            try:
                basic = float(input())
            except ValueError:
                basic = 0.0

            print("HRA : ")
            try:
                hra = float(input())
            except ValueError:
                hra = 0.0

            print("Percentage of Allowance : ")
            try:
                allowance_percentage = float(input())
            except ValueError:
                allowance_percentage = 0.0

            print("Enter Role Id : ")
            print(str(Roles.DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER.value) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER.value) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER.value) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            try:
                role = int(input())
            except ValueError:
                role = 0

            # Create empty Employee and set fields
            emp = Employee()
            emp.emp_id = emp_id
            emp.name = name
            emp.basic = basic
            emp.hra = hra
            emp.allowance_percentage = allowance_percentage
            # Store role id (as int); RoleBuilder supports enum or int
            emp.role = role

            employees[i] = emp

        print("Enter the date of the report (dd/mm/yyyy) : ")
        report_date = input()

        report = EmployeeReport(report_date)
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
