
class OurException(Exception): #Inherited from Exception Class 
    def __init__(self, message):
        self.message = message

class UsingUserException:
    def perform_division(self):
        try:
            a = float(input("Enter the numerator (a): "))
            b = float(input("Enter the denominator (b): "))

            if b == 0:
                raise OurException("b should be greater than 0, but got b = {}".format(b))
            
            d = a / b
            print(f"Division operation successful with result: {d}")
        
        except OurException as err:
            print("Raised an User defined Exception:", err.message)

ue = UsingUserException()
ue.perform_division()
