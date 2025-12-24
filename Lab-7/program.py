from result_finder import ResultFinder

class Program:
    @staticmethod
    def main(args):
                                              
        print("Enter Marks 1:")
        marks1 = int(input().strip())
        print("Enter Marks 2:")
        marks2 = int(input().strip())
        print("Enter Marks 3:")
        marks3 = int(input().strip())

                                                
        finder = ResultFinder()
        finder.set_marks1(marks1)
        finder.set_marks2(marks2)
        finder.set_marks3(marks3)

                                                                            
        finder.display_marks()
        print("Total : " + str(finder.get_total()))
        print("Average : " + str(finder.get_average()))
        print("Result : " + str(finder.get_result()))

        input()


if __name__ == "__main__":
    import sys
    Program.main(sys.argv[1:])
