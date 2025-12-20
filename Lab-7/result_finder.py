class ResultFinder:
    """
    Properties of the fields of this class
    """
    def __init__(self):
        self.marks1 = 0
        self.marks2 = 0
        self.marks3 = 0

    """
    Method to display marks obtained
    """
    def display_marks(self):
        print("Marks entered------------- ")
        print("Marks 1 : " + str(self.get_marks1()))
        print("Marks 2 : " + str(self.get_marks2()))
        print("Marks 3 : " + str(self.get_marks3()))

    """
    Method to get the total of the marks in subjects
    """
    def get_total(self):
        return self.marks1 + self.marks2 + self.marks3

    """
    Method to calculate the average of the marks
    """
    def get_average(self):
        return self.get_total() / 3.0

    """
    Method to get the result for the marks given
    """
    def get_result(self):
        if self.marks1 < 35 or self.marks2 < 35 or self.marks3 < 35:
            return "Fail"
        return "Pass"

    """
    Setters and Getters for marks
    """
    def set_marks1(self, value):
        self.marks1 = int(value)

    def set_marks2(self, value):
        self.marks2 = int(value)

    def set_marks3(self, value):
        self.marks3 = int(value)

    def get_marks1(self):
        return self.marks1

    def get_marks2(self):
        return self.marks2

    def get_marks3(self):
        return self.marks3
