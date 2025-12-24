class AccountManager:
    """
    Method to store account details into the account object passed
    """
    def fill_account_data(self, acc):
        acc.acc_no = input("Enter account number: ")
        acc.name = input("Enter account holder name: ")
        try:
            acc.balance = float(input("Enter account balance: "))
        except ValueError:
            acc.balance = 0.0

    """
    Method to display account details from the account object passed
    """
    def display_account_data(self, acc):
        print() 
        print("AccNo : " + acc.acc_no)
        print("Name : " + acc.name)
        print("Balance : " + str(acc.balance))
