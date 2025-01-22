class Calculator:
    # Class attribute that defines the type of calculations performed by this class
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.

        This method takes two numerical inputs and returns their sum.
        
        Parameters:
        a (int or float): The first number to be added.
        b (int or float): The second number to be added.

        Returns:
        int or float: The sum of a and b.
        """
        return a + b  # Return the result of adding a and b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.

        This method prints the type of calculation being performed and then
        returns the product of the two numbers.

        Parameters:
        cls: The class itself (Calculator), allowing access to class attributes.
        a (int or float): The first number to be multiplied.
        b (int or float): The second number to be multiplied.

        Returns:
        int or float: The product of a and b.
        """
        # Print the type of calculation being performed
        print(f"Calculation type: {cls.calculation_type}")
        return a * b  # Return the result of multiplying a and b
