#Модуль реализует алгоритм теории делимости
import math as math
''' 
Испытание на делимость - самое простое детерминированное
испытание. В его основе лежит использование в качестве делителей
всех чисел меньших, чем sqr(n) . Если любое из этих чисел делит n, то
n - составное число.

'''

class Number():
    number = int()
    def __init__(self):
        pass

    def setNumber(self):
        ''' Set the number to be tested! 
            --------
            Args:
                none

            Returns:
                void
         '''
        self.number = int(input("Введите число на проверку:  "))
        return self.number 
    def getNumber(self):
       ''' 
       Getter for the number
        ----------
        Args:
            None
        
        Returns:
            number: a number written by the setNumber()
       '''
       return number

    def divisible(self,n:int):
        '''
        Method to determine divisibility of a number.
        ---------
        This method will determine if a number is a simple number or not by using it's square root and dividing the number will all
        the numbers smaller than the sqr(n) with n itself. If there is any number in that spectrum divisible by n, it means that
        our n is not a simple number.

        Args:
            n(int): A number to be checked.

        Returns:
            result(string): A message showing weather n is a simple number or not
        '''
 
        test_num = math.sqrt(n)
        message = " "
        for i in range(3,int(test_num)):
           if(i %2 !=0 and i <test_num):
               result = n % i
               if result == 0:
                   print("Число {0} составное".format(n))
               if i == test_num:
                   print ("Число {0} простое")


test = Number()
byte = test.setNumber()
test.divisible(byte)