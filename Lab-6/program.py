from swap_data import SwapData

class Program:
    @staticmethod
    def main(args):
                                     
        print("Enter Number 1 : ")
        number1 = input()

        print("Enter Number 2 : ")
        number2 = input()

                                                         
        obj = SwapData()
        obj.number1 = number1
        obj.number2 = number2

                                         
        obj.display_values("Numbers before Swapping :")
        
                                            
        obj.swap_values()

                                        
        obj.display_values("Numbers after Swapping :")

        input()


if __name__ == "__main__":
    Program.main([])
