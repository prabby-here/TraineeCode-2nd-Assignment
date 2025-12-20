class Cache:
    _MAX_CAPACITY = 0

    """
    Static method to get the maximum capacity of the cache
    """
    @staticmethod
    def get_max_capacity():
        if Cache._MAX_CAPACITY <= 0:
            while True:
                try:
                    value =int(input("Enter MAX_CAPACITY (positive integer): "))
                    if value > 0:
                        Cache._MAX_CAPACITY = value
                        break
                    else:
                        print("Please enter a positive integer greater than 0.")
                except ValueError:
                    print("Invalid input. Please enter a positive integer.")
        print("Returning MAX_CAPACITY")
        return Cache._MAX_CAPACITY
