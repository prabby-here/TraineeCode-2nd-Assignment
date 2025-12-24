from employee_report import EmployeeReport
from role_builder import RoleBuilder
from roles import Roles
from employee import Employee

class Program:
    @staticmethod
    def main(args):
                                                           
        employees = [None] * 4
        emp = None

        emp_id = ""
        name = ""
        report_date = ""
        allowance_percentage = 0.0
        basic = 0.0
        hra = 0.0
        role = 0

                                                   
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
            print(str(Roles.DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.DEVELOPER))
            print(str(Roles.TEST_ENGINEER) + ". " + RoleBuilder.get_role_description(Roles.TEST_ENGINEER))
            print(str(Roles.SR_DEVELOPER) + ". " + RoleBuilder.get_role_description(Roles.SR_DEVELOPER))
            print(str(Roles.DESIGNER) + ". " + RoleBuilder.get_role_description(Roles.DESIGNER))
            try:
                role = int(input())
            except ValueError:
                role = 0

            employees[i] = Employee(emp_id, name, basic, hra, allowance_percentage, role)

        print("Enter the date of the report (dd/mm/yyyy) : ")
        report_date = input()

        report = EmployeeReport()
        report.report_date = report_date
        report.display_employees(employees)

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
