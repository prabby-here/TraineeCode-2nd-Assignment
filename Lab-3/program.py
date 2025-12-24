from employee import Employee
from address import Address

class Program:
    @staticmethod
    def main(args):
        emp = Employee()
        Program.store_data(emp)
        Program.show_data(emp)

    @staticmethod
    def store_data(emp):
                                      
        print("Enter Employee Information:")
        emp.emp_id = input("Employee Id: ").strip()
        emp.emp_name = input("Employee Name: ").strip()
        emp.emp_gender = input("Employee Gender: ").strip()

                                     
        print("Enter Employee Address:")
        address1 = input("Address 1: ").strip()
        address2 = input("Address 2: ").strip()
        city = input("City: ").strip()
        pincode = input("PinCode: ").strip()

                                              
        emp.address = Address(address1, address2, city, pincode)

    @staticmethod
    def show_data(emp):
                                                          
        print("\n---------------- Employee Information ----------------")
        print("Employee Id :", emp.emp_id)
        print("Employee Name :", emp.emp_name)
        print("Employee Gender :", emp.emp_gender)

        print("\nEmployee Address : --------------")
        if emp.address is not None:
            print("Address 1 :", emp.address.address1)
            print("Address 2 :", emp.address.address2)
            print("City :", emp.address.city)
            print("PinCode :", emp.address.pincode)
        else:
            print("No address on file")
        print("----------------------------------")


if __name__ == "__main__":
    Program.main([])
